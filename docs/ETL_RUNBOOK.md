# Retail Intelligence Platform - ETL Runbook

## 1. Purpose

This runbook explains how to run, monitor, validate, and troubleshoot the Retail Intelligence Platform ETL pipeline.

The pipeline reads Excel source files, validates data, loads SQL Server staging tables, executes warehouse procedures, validates post-load results, and creates audit logs, technical logs, and Excel summary reports.

---

## 2. Project Location

Run all commands from:

```powershell
C:\Users\uuuu\Retail_Intelligence_Platform\02_python_etl
```

---

## 3. Activate Virtual Environment

```powershell
.venv\Scripts\activate
```

Expected prompt:

```text
(.venv) PS C:\Users\uuuu\Retail_Intelligence_Platform\02_python_etl>
```

---

## 4. Install Requirements

```powershell
python -m pip install -r requirements.txt
```

---

## 5. Generate Sample Source Files

```powershell
python -m utils.generate_sample_excel_files
```

This creates sample Excel files inside:

```text
input_files
```

Expected source file types:

- product_master
- location_master
- supplier_master
- sales
- inventory_snapshot
- inventory_movement
- purchase_orders
- goods_receipts
- transfers
- forecast
- stock_optimization

---

## 6. Run Full ETL Pipeline

Production-style run:

```powershell
python main.py
```

This performs:

```text
1. Read source files
2. Validate schema
3. Validate data quality
4. Load staging tables
5. Execute DW stored procedures
6. Run post-load validation
7. Create audit records
8. Create technical log file
9. Create Excel run summary report
10. Move successful files to processed_files
```

---

## 7. Run Without Moving Files

Use this during testing:

```powershell
python main.py --skip-file-move
```

This keeps source files inside `input_files`.

---

## 8. Run Without Post-Load Validation

```powershell
python main.py --skip-post-validation
```

Use only for debugging.

---

## 9. Run Without Mart Validation

```powershell
python main.py --skip-mart-validation
```

This still validates fact table row counts but skips mart view row counts.

---

## 10. Run with Manual Batch ID

```powershell
python main.py --batch-id 262001105
```

Use carefully. Normally the system should generate batch IDs automatically.

---

## 11. Show CLI Help

```powershell
python main.py --help
```

---

## 12. Check Latest Logs

```powershell
Get-ChildItem logs -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

Open latest log folder:

```powershell
explorer logs
```

---

## 13. Check Latest Summary Reports

```powershell
Get-ChildItem reports -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

Open report folder:

```powershell
explorer reports
```

---

## 14. Check Error Reports

Error reports are created only when validation fails.

```powershell
Get-ChildItem error_reports -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

Open folder:

```powershell
explorer error_reports
```

---

## 15. Check Processed Files

```powershell
explorer processed_files
```

Files are stored like:

```text
processed_files/<file_type>/<batch_id>/<source_file>
```

---

## 16. Check Rejected Files

```powershell
explorer rejected_files
```

Files are stored like:

```text
rejected_files/<file_type>/<batch_id>/<source_file>
```

---

## 17. SQL Audit Checks

Run in SQL Server:

```sql
USE RetailIntelligenceDW;
GO

SELECT TOP 10 *
FROM audit.etl_batch_log
ORDER BY started_at DESC;

SELECT TOP 50 *
FROM audit.etl_file_log
ORDER BY created_at DESC;

SELECT TOP 50 *
FROM audit.data_quality_error_log
ORDER BY created_at DESC;
```

---

## 18. DW Fact Row Count Checks

```sql
USE RetailIntelligenceDW;
GO

SELECT COUNT(*) AS rows_count FROM dw.fact_sales;
SELECT COUNT(*) AS rows_count FROM dw.fact_inventory_snapshot;
SELECT COUNT(*) AS rows_count FROM dw.fact_inventory_movement;
SELECT COUNT(*) AS rows_count FROM dw.fact_purchase_orders;
SELECT COUNT(*) AS rows_count FROM dw.fact_goods_receipts;
SELECT COUNT(*) AS rows_count FROM dw.fact_transfers;
SELECT COUNT(*) AS rows_count FROM dw.fact_forecast;
SELECT COUNT(*) AS rows_count FROM dw.fact_stock_optimization;
```

---

## 19. Mart View Checks

```sql
USE RetailIntelligenceDW;
GO

SELECT COUNT(*) AS rows_count FROM mart.vw_sales_performance;
SELECT COUNT(*) AS rows_count FROM mart.vw_inventory_position;
SELECT COUNT(*) AS rows_count FROM mart.vw_latest_inventory_position;
SELECT COUNT(*) AS rows_count FROM mart.vw_inventory_movement_analysis;
SELECT COUNT(*) AS rows_count FROM mart.vw_purchase_order_analysis;
SELECT COUNT(*) AS rows_count FROM mart.vw_goods_receipt_analysis;
SELECT COUNT(*) AS rows_count FROM mart.vw_transfer_analysis;
SELECT COUNT(*) AS rows_count FROM mart.vw_forecast_accuracy;
SELECT COUNT(*) AS rows_count FROM mart.vw_stock_optimization;
SELECT COUNT(*) AS rows_count FROM mart.vw_executive_kpi_base;
```

---

## 20. Common Issue: No Files Found

Reason:

```text
input_files folders are empty
```

Fix:

```powershell
python -m utils.generate_sample_excel_files
```

---

## 21. Common Issue: Source Files Were Moved

Reason:

```text
The pipeline ran successfully and moved files to processed_files
```

Fix:

Generate files again:

```powershell
python -m utils.generate_sample_excel_files
```

Or test using:

```powershell
python main.py --skip-file-move
```

---

## 22. Common Issue: Data Quality Failed

Reason:

```text
One or more rows failed validation
```

Check:

```text
error_reports
audit.data_quality_error_log
logs
```

Fix the source file and rerun.

---

## 23. Common Issue: Post-Load Validation Failed

Reason:

```text
Fact table or mart view row counts did not match expectation
```

Check:

```text
logs
reports
audit tables
DW stored procedures
mart views
```

---

## 24. Recommended Testing Flow

```powershell
python -m utils.generate_sample_excel_files
python main.py --skip-file-move
Get-ChildItem logs -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
Get-ChildItem reports -File | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

---

## 25. Recommended Production Flow

```powershell
python -m utils.generate_sample_excel_files
python main.py
```

This will process files and move them to `processed_files`.

---

## 26. Expected Successful Result

A successful run should show:

```text
ETL pipeline completed successfully.
Post-load validation passed.
ETL LOGGING COMPLETED
```

Reports should appear in:

```text
reports
```

Logs should appear in:

```text
logs
```
