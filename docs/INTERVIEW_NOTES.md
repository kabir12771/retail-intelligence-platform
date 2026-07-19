# Retail Intelligence Platform - Interview Notes

## 1. Short Project Explanation

I built an end-to-end Retail Intelligence Platform for fashion retail analytics.

The project reads ERP-style Excel files, validates schema and data quality, loads clean data into SQL Server staging tables, executes stored procedures to populate a dimensional data warehouse, and exposes Power BI-ready mart views.

It also includes audit tables, technical logs, Excel run summary reports, rejected row reports, processed/rejected file movement, environment configuration, and command-line execution.

---

## 2. Business Problem

Retail businesses often have fragmented data across sales files, inventory files, purchase orders, goods receipts, transfers, forecasts, and stock optimization files.

This causes:

- Manual reporting
- Delayed decision-making
- Poor inventory visibility
- Weak stock allocation
- Limited audit trail
- Low confidence in reports
- No rejected-data process

My project solves this by creating a structured, validated, auditable data platform.

---

## 3. Architecture Explanation

The architecture is:

```text
Excel / ERP files
→ Python ETL
→ SQL Server staging
→ SQL Server data warehouse
→ Mart views
→ Power BI dashboards
```

Python handles orchestration, file reading, validation, logging, reporting, and file movement.

SQL Server handles staging, warehouse loading, dimensional modeling, stored procedures, and mart views.

---

## 4. Why I Used SQL Server

I used SQL Server because it is widely used in enterprise environments and works well for:

- Data warehousing
- Stored procedures
- Relational modeling
- Audit tables
- Power BI connectivity
- Structured business reporting

---

## 5. Why I Used Python

I used Python because it is strong for:

- Reading Excel files
- Data cleaning
- Validation
- Automation
- Logging
- Report generation
- ETL orchestration

Python controls the pipeline, while SQL Server manages warehouse loading and reporting structures.

---

## 6. Why I Used Staging Tables

Staging tables separate source data from final warehouse data.

Benefits:

- Safer loading process
- Easier troubleshooting
- Batch-level traceability
- Better validation
- Re-runnable ETL
- Clean separation between source and warehouse

---

## 7. Why I Used Stored Procedures

Stored procedures keep warehouse transformation logic inside SQL Server.

Benefits:

- Better performance
- Easier database maintenance
- Clear warehouse loading logic
- Centralized SQL business rules
- Better control over dimension and fact loading

---

## 8. Data Warehouse Design

The project uses a dimensional warehouse model.

Main dimensions:

- Product
- Location
- Supplier
- Calendar
- Channel
- Promotion
- Movement type
- Status
- Forecast model
- Optimization model

Main facts:

- Sales
- Inventory snapshot
- Inventory movement
- Purchase orders
- Goods receipts
- Transfers
- Forecast
- Stock optimization

---

## 9. Fact Table Grain Explanation

Each fact table has a defined business grain.

Examples:

- `fact_sales`: one sales transaction line
- `fact_inventory_snapshot`: one product-location-date stock snapshot
- `fact_purchase_orders`: one purchase order line
- `fact_goods_receipts`: one goods receipt line
- `fact_transfers`: one transfer document line
- `fact_forecast`: one forecast record per product-location-period
- `fact_stock_optimization`: one optimization result per product-location-run

This makes the model reliable for Power BI reporting.

---

## 10. Validation Framework

The ETL includes three validation layers.

### Schema Validation

Checks whether required columns exist.

### Data Quality Validation

Checks:

- Missing values
- Invalid dates
- Invalid numbers
- Negative values
- Duplicate business keys
- Invalid status codes
- Business rule mismatches

### Post-Load Validation

Checks:

- Audit batch status
- File log count
- DW fact row counts
- Mart view row counts

---

## 11. Audit and Logging Explanation

The project has three evidence layers:

| Evidence | Purpose |
|---|---|
| SQL audit tables | Track batch and file processing |
| Technical log files | Troubleshoot pipeline runs |
| Excel summary reports | Business-friendly run summary |

This makes the pipeline more production-like and supportable.

---

## 12. Error Handling Explanation

If a file fails validation:

- It does not load into the warehouse.
- An error report is created.
- Rejected rows are logged.
- The batch is marked failed.
- Failed source files can be moved to `rejected_files`.

This protects the warehouse from bad data.

---

## 13. File Movement Explanation

After successful processing:

```text
input_files → processed_files
```

After failed processing:

```text
input_files → rejected_files
```

Files are organized by:

```text
file_type / batch_id / source_file
```

This creates a full operational history.

---

## 14. Business Metrics Supported

The platform supports:

- Sales quantity
- Net sales amount
- Gross margin
- Stock on hand
- Available stock
- Inventory value
- Stock cover
- Ordered quantity
- Open quantity
- Received quantity
- Transfer in-transit quantity
- Forecast accuracy
- Forecast bias
- Safety stock
- Reorder point
- Recommended order quantity
- Inventory health score

---

## 15. Power BI Readiness

Power BI can connect directly to the mart views.

Important mart views:

- `mart.vw_sales_performance`
- `mart.vw_inventory_position`
- `mart.vw_latest_inventory_position`
- `mart.vw_purchase_order_analysis`
- `mart.vw_goods_receipt_analysis`
- `mart.vw_transfer_analysis`
- `mart.vw_forecast_accuracy`
- `mart.vw_stock_optimization`
- `mart.vw_executive_kpi_base`

---

## 16. What Makes This Project Strong

This is not only a dashboard project.

It includes:

- SQL Server warehouse design
- Python ETL pipeline
- Schema validation
- Data quality validation
- SQL stored procedures
- Audit logs
- Technical logs
- Excel run reports
- Error reports
- File movement automation
- Mart views for Power BI
- CLI arguments
- Environment configuration

---

## 17. Interview Pitch

I built a complete Retail Intelligence Platform for fashion retail and supply chain analytics.

It reads ERP-style Excel files, validates data, loads SQL Server staging tables, executes stored procedures to populate a dimensional warehouse, and exposes mart views for Power BI dashboards.

I also implemented audit logging, technical logs, error reports, Excel run summaries, command-line controls, and processed/rejected file movement.

The project supports sales, inventory, purchase orders, goods receipts, transfers, forecasting, and stock optimization analytics.

---

## 18. Example Interview Answer

Question: What was your role in this project?

Answer:

I designed and built the full data foundation. I created the SQL Server schemas, dimensions, fact tables, staging tables, warehouse load procedures, mart views, and Python ETL pipeline. I also built schema validation, data quality checks, audit logging, technical logs, Excel summary reports, error reports, and file movement automation.

---

## 19. Example Interview Answer

Question: How do you ensure data quality?

Answer:

I validate the data in three layers. First, schema validation checks whether required columns exist. Second, data quality validation checks required values, dates, numbers, duplicates, allowed values, and business rules. Third, post-load validation checks audit status, file log count, fact table row counts, and mart view row counts.

---

## 20. Example Interview Answer

Question: Why did you create mart views?

Answer:

Mart views simplify reporting. Instead of connecting Power BI directly to raw warehouse tables, I created business-friendly views that already include useful joins and metrics. This makes dashboards easier to build and keeps reporting logic consistent.

---

## 21. Example Interview Answer

Question: How would this project help a retail business?

Answer:

It gives the business one trusted source of truth for sales, inventory, purchase orders, goods receipts, transfers, forecasts, and stock optimization. It reduces manual reporting, improves auditability, and prepares clean data for Power BI dashboards and planning decisions.

---

## 22. Future Enhancements

Future enhancements include:

- Power BI executive dashboard
- Demand forecasting engine
- Inventory optimization engine
- AI supply chain assistant
- Flask web application
- Azure deployment
- GitHub portfolio publishing
- Final project PDF book
