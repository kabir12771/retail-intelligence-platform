# Retail Intelligence Platform - Architecture

## 1. Architecture Overview

The Retail Intelligence Platform is designed as an enterprise-style retail analytics architecture.

It converts operational Excel and ERP-style source files into a clean SQL Server Data Warehouse and Power BI-ready reporting layer.

```text
Excel / ERP Source Files
        ↓
Python ETL Pipeline
        ↓
Schema + Data Quality Validation
        ↓
SQL Server Staging Tables
        ↓
SQL Server Stored Procedures
        ↓
Dimensional Data Warehouse
        ↓
Mart Views
        ↓
Power BI Dashboards
```

---

## 2. Source Layer

The source layer contains operational business files.

Supported file types:

- Product master
- Location master
- Supplier master
- Sales
- Inventory snapshot
- Inventory movement
- Purchase orders
- Goods receipts
- Transfers
- Forecast
- Stock optimization

Each file type has its own folder inside `input_files`.

---

## 3. Python ETL Layer

The Python ETL layer controls the pipeline execution.

Main responsibilities:

- Read Excel files
- Standardize column names
- Validate required columns
- Validate data quality
- Load valid data to SQL staging tables
- Export error reports
- Execute warehouse stored procedures
- Run post-load validation
- Generate technical logs
- Generate Excel run summary reports
- Move processed and rejected files

Main entry point:

```text
main.py
```

---

## 4. Configuration Layer

Configuration is handled through:

- `.env`
- `config/database_config.py`
- `config/file_config.py`
- `config/column_mapping.py`
- `config/pipeline_config.py`
- `utils/cli_args.py`

This makes the pipeline flexible and easier to run in different environments.

Example environments:

- dev
- test
- prod

---

## 5. SQL Server Layer

The SQL Server database is divided into schemas.

| Schema | Purpose |
|---|---|
| raw | Raw source data layer |
| stg | Validated staging data |
| dw | Dimensional warehouse tables |
| mart | Power BI-ready reporting views |
| audit | ETL audit and error tracking |

---

## 6. Staging Layer

The staging layer stores validated data before warehouse loading.

Examples:

- `stg.product`
- `stg.location`
- `stg.supplier`
- `stg.sales`
- `stg.inventory_snapshot`
- `stg.inventory_movement`
- `stg.purchase_orders`
- `stg.goods_receipts`
- `stg.transfers`
- `stg.forecast`
- `stg.stock_optimization`

Each staging table includes technical columns such as:

- batch_id
- source_file_name
- source_row_number
- is_valid
- validation_message
- created_at

---

## 7. Data Warehouse Layer

The warehouse uses dimensional modeling.

### Dimension Tables

- `dw.dim_product`
- `dw.dim_location`
- `dw.dim_supplier`
- `dw.dim_calendar`
- `dw.dim_channel`
- `dw.dim_promotion`
- `dw.dim_movement_type`
- `dw.dim_status`
- `dw.dim_forecast_model`
- `dw.dim_optimization_model`

### Fact Tables

- `dw.fact_sales`
- `dw.fact_inventory_snapshot`
- `dw.fact_inventory_movement`
- `dw.fact_purchase_orders`
- `dw.fact_goods_receipts`
- `dw.fact_transfers`
- `dw.fact_forecast`
- `dw.fact_stock_optimization`

---

## 8. Mart Layer

The mart layer exposes reporting-ready SQL views.

Power BI can connect directly to these views.

Examples:

- `mart.vw_sales_performance`
- `mart.vw_inventory_position`
- `mart.vw_latest_inventory_position`
- `mart.vw_inventory_movement_analysis`
- `mart.vw_purchase_order_analysis`
- `mart.vw_goods_receipt_analysis`
- `mart.vw_transfer_analysis`
- `mart.vw_forecast_accuracy`
- `mart.vw_stock_optimization`
- `mart.vw_executive_kpi_base`

---

## 9. Audit Architecture

The audit layer tracks every ETL run.

Audit tables:

- `audit.etl_batch_log`
- `audit.etl_file_log`
- `audit.data_quality_error_log`

These tables answer:

- When did the pipeline run?
- Which files were processed?
- How many rows were read?
- How many rows were loaded?
- Which rows failed validation?
- What was the final batch status?

---

## 10. Logging Architecture

Each run creates a technical log file inside:

```text
logs
```

The log captures:

- Runtime configuration
- File processing details
- Validation results
- Staging load results
- DW stored procedure execution
- Post-load validation
- File movement
- Errors and exceptions

---

## 11. Reporting Architecture

Each run creates an Excel summary report inside:

```text
reports
```

The report includes:

- Run summary
- File-level results
- Post-load validation results
- Runtime configuration

---

## 12. File Movement Architecture

After successful processing:

```text
input_files → processed_files
```

After failed validation:

```text
input_files → rejected_files
```

Folder structure:

```text
processed_files/<file_type>/<batch_id>/<source_file>
rejected_files/<file_type>/<batch_id>/<source_file>
```

---

## 13. Design Principles

This architecture follows these principles:

- Separation of concerns
- Validation before loading
- Batch-level auditability
- Re-runnable execution
- Config-driven pipeline behavior
- SQL Server for warehouse logic
- Python for orchestration and file handling
- Mart views for BI consumption
- Error isolation through rejected files and reports
