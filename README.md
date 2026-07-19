<!-- PORTFOLIO_HEADER_START -->

<p align="center">
  <h1 align="center">Retail Intelligence Platform</h1>
  <p align="center">
    End-to-End Retail Data Warehouse, Python ETL, Data Quality Validation, Audit Logging, and Power BI-Ready Analytics Platform
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-ETL-blue" />
  <img src="https://img.shields.io/badge/SQL%20Server-Data%20Warehouse-red" />
  <img src="https://img.shields.io/badge/Power%20BI-Ready-yellow" />
  <img src="https://img.shields.io/badge/Data%20Quality-Validation-green" />
  <img src="https://img.shields.io/badge/Retail-Supply%20Chain-purple" />
  <img src="https://img.shields.io/badge/Status-Active%20Portfolio%20Project-brightgreen" />
</p>

---

## Portfolio Summary

Retail Intelligence Platform is a professional, end-to-end analytics engineering project designed for fashion retail, inventory control, supply chain analytics, merchandise planning, and business intelligence.

The platform simulates a real enterprise data pipeline that reads operational Excel and ERP-style files, validates data quality, loads SQL Server staging tables, executes warehouse stored procedures, and exposes Power BI-ready mart views.

This project demonstrates practical skills in:

- Retail analytics and supply chain reporting
- Python ETL development
- SQL Server data warehouse design
- Dimensional modeling
- Data quality validation
- Audit logging and operational monitoring
- Error reporting and rejected file handling
- Power BI-ready mart view design
- GitHub-ready project documentation

---

## Table of Contents

- [Project Overview](#1-project-overview)
- [Business Problem](#2-business-problem)
- [Business Objective](#3-business-objective)
- [High-Level Architecture](#4-high-level-architecture)
- [Project Status](#5-project-status)
- [Project Folder Structure](#6-project-folder-structure)
- [SQL Server Database Design](#7-sql-server-database-design)
- [Data Warehouse Model](#8-data-warehouse-model)
- [ETL Pipeline Flow](#9-etl-pipeline-flow)
- [Supported Source Files](#10-supported-source-files)
- [Validation Framework](#11-validation-framework)
- [Audit, Logs, and Reports](#12-audit-logs-and-reports)
- [File Movement Logic](#13-file-movement-logic)
- [Configuration](#14-configuration)
- [Command-Line Arguments](#15-command-line-arguments)
- [Setup Instructions](#16-setup-instructions)
- [Testing Commands](#17-testing-commands)
- [SQL Audit Queries](#18-sql-audit-queries)
- [Mart Views for Power BI](#19-mart-views-for-power-bi)
- [Business Metrics Supported](#20-business-metrics-supported)
- [Portfolio Explanation](#21-portfolio-explanation)
- [Interview Explanation](#22-interview-explanation)
- [Future Enhancements](#23-future-enhancements)
- [Current Progress](#24-current-progress)
- [Author](#25-author)

---

## Key Capabilities

| Capability | Description |
|---|---|
| Python ETL | Reads, validates, and loads Excel source files |
| SQL Server Warehouse | Stores clean dimensional data using facts and dimensions |
| Validation Framework | Checks schema, data quality, business rules, and post-load results |
| Audit Logging | Tracks batch status, file status, row counts, and errors |
| Error Reports | Creates Excel reports for rejected rows |
| Run Summary Reports | Creates business-friendly Excel reports after each ETL run |
| File Movement | Moves processed and rejected files into controlled folders |
| Power BI-Ready Views | Provides mart views for dashboard development |
| GitHub Documentation | Includes README, architecture notes, runbook, and interview notes |

---

<!-- PORTFOLIO_HEADER_END -->
\# Retail Intelligence Platform



\## End-to-End Retail Data Warehouse, ETL, Validation, Audit, and Power BI-Ready Analytics Platform



\---



\## 1. Project Overview



\*\*Retail Intelligence Platform\*\* is an end-to-end enterprise analytics project designed for fashion retail, merchandise planning, inventory control, supply chain analytics, and business intelligence.



The project simulates a real retail company environment where operational data comes from ERP systems, Excel files, warehouse records, sales transactions, stock snapshots, purchase orders, goods receipts, store transfers, forecasts, and stock optimization outputs.



The goal of the project is to convert fragmented operational data into a clean, validated, auditable, Power BI-ready SQL Server Data Warehouse.



This project is built using:



| Layer                 | Technology                  |

| --------------------- | --------------------------- |

| Source Files          | Excel                       |

| ETL Orchestration     | Python                      |

| Data Processing       | pandas                      |

| Database              | Microsoft SQL Server        |

| SQL Connectivity      | SQLAlchemy + pyodbc         |

| Data Warehouse Design | Star Schema                 |

| Validation            | Python Validation Framework |

| Audit                 | SQL Server Audit Tables     |

| Logging               | Python Log Files            |

| Reports               | Excel Run Summary Reports   |

| BI Layer              | Power BI-Ready Mart Views   |



\---



\## 2. Business Problem



Retail companies often manage data across multiple disconnected systems and files.



Typical data sources include:



\* Product master files

\* Store and warehouse master files

\* Supplier master files

\* Sales transactions

\* Inventory snapshots

\* Inventory movement records

\* Purchase orders

\* Goods receipts

\* Inter-store transfers

\* Forecast files

\* Stock optimization outputs



This creates many business problems:



\* No single version of truth

\* Manual Excel reporting

\* Delayed visibility of stock and sales

\* Poor stock allocation decisions

\* Difficulty tracking purchase orders and goods receipts

\* Weak transfer visibility between stores and warehouses

\* Limited forecast accuracy tracking

\* No proper validation before reporting

\* No audit trail for file processing

\* No rejected-row investigation process

\* No structured foundation for Power BI dashboards



\---



\## 3. Business Objective



The objective of this project is to build a professional retail analytics platform that can:



1\. Read operational Excel source files.

2\. Standardize and validate incoming data.

3\. Reject bad data before it reaches the warehouse.

4\. Load clean data into SQL Server staging tables.

5\. Execute stored procedures to populate warehouse dimensions and facts.

6\. Refresh Power BI-ready mart views.

7\. Track every ETL batch with audit tables.

8\. Save full technical logs for troubleshooting.

9\. Generate Excel run summary reports.

10\. Generate error reports for rejected rows.

11\. Move successful files to processed folders.

12\. Move failed files to rejected folders.

13\. Create a scalable foundation for forecasting, optimization, and AI analytics.



\---



\## 4. High-Level Architecture



```text

Excel / ERP Source Files

&#x20;       â†“

Python ETL Pipeline

&#x20;       â†“

Schema Validation

&#x20;       â†“

Data Quality Validation

&#x20;       â†“

SQL Server Staging Tables

&#x20;       â†“

SQL Stored Procedures

&#x20;       â†“

SQL Server Data Warehouse

&#x20;       â†“

Mart Views

&#x20;       â†“

Power BI Dashboards

&#x20;       â†“

Forecasting + Inventory Optimization + AI Assistant

```



\---



\## 5. Project Status



Current completed builds:



| Build Area                       | Status    |

| -------------------------------- | --------- |

| SQL Server database creation     | Completed |

| Database schemas                 | Completed |

| Core dimensions                  | Completed |

| Core fact tables                 | Completed |

| Staging tables                   | Completed |

| DW load stored procedures        | Completed |

| Mart views                       | Completed |

| Sample Excel data generator      | Completed |

| Python virtual environment       | Completed |

| SQL Server connection            | Completed |

| Excel reader                     | Completed |

| Schema validation                | Completed |

| Data quality validation          | Completed |

| SQL staging loader               | Completed |

| DW procedure executor            | Completed |

| Main ETL runner                  | Completed |

| Audit logging                    | Completed |

| Error report export              | Completed |

| Processed/rejected file movement | Completed |

| Post-load validation             | Completed |

| Environment-based configuration  | Completed |

| Command-line arguments           | Completed |

| Professional logging system      | Completed |

| Pipeline run summary report      | Completed |



\---



\## 6. Project Folder Structure



```text

Retail\_Intelligence\_Platform

â”‚

â”œâ”€â”€ 01\_database\_design

â”‚   â””â”€â”€ sql\_scripts

â”‚

â””â”€â”€ 02\_python\_etl

&#x20;   â”‚

&#x20;   â”œâ”€â”€ audit

&#x20;   â”‚   â”œâ”€â”€ \_\_init\_\_.py

&#x20;   â”‚   â””â”€â”€ audit\_logger.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ config

&#x20;   â”‚   â”œâ”€â”€ column\_mapping.py

&#x20;   â”‚   â”œâ”€â”€ database\_config.py

&#x20;   â”‚   â”œâ”€â”€ file\_config.py

&#x20;   â”‚   â””â”€â”€ pipeline\_config.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ docs

&#x20;   â”‚   â”œâ”€â”€ ARCHITECTURE.md

&#x20;   â”‚   â”œâ”€â”€ ETL\_RUNBOOK.md

&#x20;   â”‚   â””â”€â”€ INTERVIEW\_NOTES.md

&#x20;   â”‚

&#x20;   â”œâ”€â”€ error\_reports

&#x20;   â”‚

&#x20;   â”œâ”€â”€ extract

&#x20;   â”‚   â””â”€â”€ read\_excel.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ input\_files

&#x20;   â”‚   â”œâ”€â”€ product\_master

&#x20;   â”‚   â”œâ”€â”€ location\_master

&#x20;   â”‚   â”œâ”€â”€ supplier\_master

&#x20;   â”‚   â”œâ”€â”€ sales

&#x20;   â”‚   â”œâ”€â”€ inventory\_snapshot

&#x20;   â”‚   â”œâ”€â”€ inventory\_movement

&#x20;   â”‚   â”œâ”€â”€ purchase\_orders

&#x20;   â”‚   â”œâ”€â”€ goods\_receipts

&#x20;   â”‚   â”œâ”€â”€ transfers

&#x20;   â”‚   â”œâ”€â”€ forecast

&#x20;   â”‚   â””â”€â”€ stock\_optimization

&#x20;   â”‚

&#x20;   â”œâ”€â”€ load

&#x20;   â”‚   â”œâ”€â”€ sql\_connection.py

&#x20;   â”‚   â”œâ”€â”€ staging\_loader.py

&#x20;   â”‚   â””â”€â”€ dw\_loader.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ logs

&#x20;   â”‚

&#x20;   â”œâ”€â”€ processed\_files

&#x20;   â”‚

&#x20;   â”œâ”€â”€ rejected\_files

&#x20;   â”‚

&#x20;   â”œâ”€â”€ reports

&#x20;   â”‚

&#x20;   â”œâ”€â”€ tests

&#x20;   â”‚

&#x20;   â”œâ”€â”€ transform

&#x20;   â”‚

&#x20;   â”œâ”€â”€ utils

&#x20;   â”‚   â”œâ”€â”€ cli\_args.py

&#x20;   â”‚   â”œâ”€â”€ error\_report\_exporter.py

&#x20;   â”‚   â”œâ”€â”€ file\_mover.py

&#x20;   â”‚   â”œâ”€â”€ generate\_sample\_excel\_files.py

&#x20;   â”‚   â”œâ”€â”€ pipeline\_logger.py

&#x20;   â”‚   â””â”€â”€ run\_summary\_report.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ validate

&#x20;   â”‚   â”œâ”€â”€ data\_quality\_checks.py

&#x20;   â”‚   â”œâ”€â”€ post\_load\_validation.py

&#x20;   â”‚   â””â”€â”€ schema\_validation.py

&#x20;   â”‚

&#x20;   â”œâ”€â”€ main.py

&#x20;   â”œâ”€â”€ requirements.txt

&#x20;   â””â”€â”€ .env

```



\---



\## 7. SQL Server Database Design



The SQL Server database uses multiple schemas to separate responsibilities.



| Schema  | Purpose                           |

| ------- | --------------------------------- |

| `raw`   | Original raw data layer           |

| `stg`   | Validated staging data            |

| `dw`    | Dimensional data warehouse        |

| `mart`  | Reporting and Power BI views      |

| `audit` | ETL audit logs and error tracking |



\---



\## 8. Data Warehouse Model



The warehouse is designed using dimensional modeling principles.



\### 8.1 Dimension Tables



| Dimension                   | Purpose                                      |

| --------------------------- | -------------------------------------------- |

| `dw.dim\_product`            | Product, style, barcode, season, color, size |

| `dw.dim\_location`           | Stores, warehouses, countries, regions       |

| `dw.dim\_supplier`           | Supplier master information                  |

| `dw.dim\_calendar`           | Date intelligence                            |

| `dw.dim\_channel`            | Sales channels                               |

| `dw.dim\_promotion`          | Promotion information                        |

| `dw.dim\_movement\_type`      | Inventory movement type                      |

| `dw.dim\_status`             | Transaction and document statuses            |

| `dw.dim\_forecast\_model`     | Forecast model metadata                      |

| `dw.dim\_optimization\_model` | Stock optimization model metadata            |



\### 8.2 Fact Tables



| Fact Table                   | Business Grain                                   |

| ---------------------------- | ------------------------------------------------ |

| `dw.fact\_sales`              | One sales transaction line                       |

| `dw.fact\_inventory\_snapshot` | One product-location-date stock snapshot         |

| `dw.fact\_inventory\_movement` | One inventory movement document line             |

| `dw.fact\_purchase\_orders`    | One purchase order line                          |

| `dw.fact\_goods\_receipts`     | One goods receipt document line                  |

| `dw.fact\_transfers`          | One transfer document line                       |

| `dw.fact\_forecast`           | One forecast record per product-location-period  |

| `dw.fact\_stock\_optimization` | One optimization result per product-location-run |



\---



\## 9. ETL Pipeline Flow



The Python ETL pipeline performs the following steps:



```text

1\. Read source Excel files

2\. Standardize column names

3\. Validate required columns

4\. Validate required values

5\. Validate date fields

6\. Validate numeric fields

7\. Validate allowed values

8\. Validate duplicate business keys

9\. Validate business rules

10\. Load clean data to SQL Server staging tables

11\. Execute SQL Server DW stored procedures

12\. Run post-load validation

13\. Generate SQL audit records

14\. Generate technical log file

15\. Generate Excel run summary report

16\. Generate error report if validation fails

17\. Move successful files to processed\_files

18\. Move rejected files to rejected\_files

```



\---



\## 10. Supported Source Files



| File Type          | Folder                           |

| ------------------ | -------------------------------- |

| Product Master     | `input\_files/product\_master`     |

| Location Master    | `input\_files/location\_master`    |

| Supplier Master    | `input\_files/supplier\_master`    |

| Sales              | `input\_files/sales`              |

| Inventory Snapshot | `input\_files/inventory\_snapshot` |

| Inventory Movement | `input\_files/inventory\_movement` |

| Purchase Orders    | `input\_files/purchase\_orders`    |

| Goods Receipts     | `input\_files/goods\_receipts`     |

| Transfers          | `input\_files/transfers`          |

| Forecast           | `input\_files/forecast`           |

| Stock Optimization | `input\_files/stock\_optimization` |



\---



\## 11. Validation Framework



The project includes three validation layers.



\### 11.1 Schema Validation



Schema validation checks that required columns exist in each source file.



Examples:



\* Product code must exist in product master.

\* Sales transaction ID must exist in sales file.

\* Purchase order number must exist in purchase order file.

\* Transfer order number must exist in transfer file.



\### 11.2 Data Quality Validation



Data quality validation checks:



\* Missing required values

\* Invalid dates

\* Invalid numeric values

\* Negative values where not allowed

\* Duplicate business keys

\* Invalid status codes

\* Business rule mismatches



Examples:



\* Sales net amount must match gross amount minus discount.

\* Inventory cost value must match stock quantity multiplied by unit cost.

\* Completed transfer shortage must match shipped quantity minus received quantity.

\* In-transit transfers are not treated as shortages.



\### 11.3 Post-Load Validation



Post-load validation checks whether the warehouse was loaded correctly.



It validates:



\* Audit batch status

\* File log count

\* Fact table row counts

\* Mart view row counts



Example output:



```text

POST-LOAD VALIDATION RESULTS

PASS   Audit batch status

PASS   Audit file log count

PASS   DW fact row count

PASS   Mart view row count

Failed Checks: 0

```



\---



\## 12. Audit, Logs, and Reports



The project has three evidence layers.



| Evidence Type         | Location               | Purpose                       |

| --------------------- | ---------------------- | ----------------------------- |

| SQL Audit Tables      | `audit` schema         | Operational database history  |

| Technical Logs        | `logs` folder          | Full troubleshooting trace    |

| Excel Summary Reports | `reports` folder       | Business-friendly run summary |

| Error Reports         | `error\_reports` folder | Rejected row investigation    |



\### 12.1 SQL Audit Tables



| Table                          | Purpose                         |

| ------------------------------ | ------------------------------- |

| `audit.etl\_batch\_log`          | One row per ETL batch           |

| `audit.etl\_file\_log`           | One row per file type processed |

| `audit.data\_quality\_error\_log` | Rejected row details            |



\### 12.2 Technical Logs



Each ETL run creates a log file like:



```text

logs/262001105\_20260719\_110524\_etl\_run.log

```



The log captures:



\* Runtime configuration

\* Source files processed

\* Rows read

\* Rows loaded

\* Validation results

\* Stored procedure execution

\* Post-load validation

\* File movement

\* Errors and tracebacks



\### 12.3 Excel Summary Reports



Each ETL run creates an Excel summary report like:



```text

reports/262001105\_20260719\_110635\_etl\_run\_summary.xlsx

```



Sheets included:



\* `Run\_Summary`

\* `File\_Results`

\* `Post\_Load\_Validation`

\* `Runtime\_Config`



\---



\## 13. File Movement Logic



After successful ETL:



```text

input\_files â†’ processed\_files

```



After failed validation:



```text

input\_files â†’ rejected\_files

```



Folder structure:



```text

processed\_files/<file\_type>/<batch\_id>/<source\_file>

rejected\_files/<file\_type>/<batch\_id>/<source\_file>

```



Example:



```text

processed\_files/sales/262001105/sales\_sample.xlsx

```



\---



\## 14. Configuration



The pipeline uses `.env` for runtime configuration.



Example:



```env

DB\_SERVER=localhost\\SQLEXPRESS

DB\_NAME=RetailIntelligenceDW

DB\_DRIVER=ODBC Driver 17 for SQL Server

DB\_AUTH\_MODE=windows

DB\_USERNAME=

DB\_PASSWORD=

DB\_TRUST\_SERVER\_CERTIFICATE=yes



PIPELINE\_NAME=Retail Intelligence Platform ETL

PIPELINE\_ENV=dev



CLEAR\_STAGING\_BATCH=true

ENABLE\_POST\_LOAD\_VALIDATION=true

VALIDATE\_MART\_VIEWS=true



MOVE\_FILES\_AFTER\_SUCCESS=true

MOVE\_REJECTED\_FILES\_ON\_FAILURE=true

```



\---



\## 15. Command-Line Arguments



The pipeline supports command-line options.



Show help:



```powershell

python main.py --help

```



Available commands:



```powershell

python main.py

python main.py --env test

python main.py --skip-file-move

python main.py --skip-post-validation

python main.py --skip-mart-validation

python main.py --no-clear-staging

python main.py --batch-id 262001105

```



\### Common Run Modes



Production-style run:



```powershell

python main.py

```



Testing without moving files:



```powershell

python main.py --skip-file-move

```



Testing without mart validation:



```powershell

python main.py --skip-mart-validation

```



Testing with multiple options:



```powershell

python main.py --env test --skip-file-move --skip-mart-validation

```



\---



\## 16. Setup Instructions



\### 16.1 Create Virtual Environment



From the `02\_python\_etl` folder:



```powershell

python -m venv .venv

```



Activate:



```powershell

.venv\\Scripts\\activate

```



\### 16.2 Install Requirements



```powershell

python -m pip install -r requirements.txt

```



\### 16.3 Configure `.env`



Update `.env` with your SQL Server connection details.



Example:



```env

DB\_SERVER=localhost\\SQLEXPRESS

DB\_NAME=RetailIntelligenceDW

DB\_DRIVER=ODBC Driver 17 for SQL Server

DB\_AUTH\_MODE=windows

DB\_TRUST\_SERVER\_CERTIFICATE=yes

```



\### 16.4 Generate Sample Excel Files



```powershell

python -m utils.generate\_sample\_excel\_files

```



\### 16.5 Run Full ETL



```powershell

python main.py

```



\---



\## 17. Testing Commands



Test SQL Server connection:



```powershell

python -m tests.test\_sql\_connection

```



Test ETL configuration:



```powershell

python -m tests.test\_etl\_config

```



Test Excel reader:



```powershell

python -m tests.test\_read\_all\_excel\_files

```



Test schema validation:



```powershell

python -m tests.test\_schema\_validation

```



Test data quality checks:



```powershell

python -m tests.test\_data\_quality\_checks

```



Test staging load:



```powershell

python -m tests.test\_load\_staging

```



Test DW load:



```powershell

python -m tests.test\_load\_dw

```



Test post-load validation:



```powershell

python -m tests.test\_post\_load\_validation

```



Test error report generation:



```powershell

python -m tests.test\_error\_report\_export

```



\---



\## 18. SQL Audit Queries



Use these queries in SQL Server to check ETL history.



```sql

USE RetailIntelligenceDW;

GO



SELECT TOP 10 \*

FROM audit.etl\_batch\_log

ORDER BY started\_at DESC;



SELECT TOP 50 \*

FROM audit.etl\_file\_log

ORDER BY created\_at DESC;



SELECT TOP 50 \*

FROM audit.data\_quality\_error\_log

ORDER BY created\_at DESC;

```



\---



\## 19. Mart Views for Power BI



Power BI can connect directly to the `mart` views.



| Mart View                             | Purpose                      |

| ------------------------------------- | ---------------------------- |

| `mart.vw\_sales\_performance`           | Sales reporting              |

| `mart.vw\_inventory\_position`          | Inventory position           |

| `mart.vw\_latest\_inventory\_position`   | Latest stock view            |

| `mart.vw\_inventory\_movement\_analysis` | Inventory movement analysis  |

| `mart.vw\_purchase\_order\_analysis`     | Purchase order monitoring    |

| `mart.vw\_goods\_receipt\_analysis`      | Goods receipt tracking       |

| `mart.vw\_transfer\_analysis`           | Transfer analysis            |

| `mart.vw\_forecast\_accuracy`           | Forecast accuracy analysis   |

| `mart.vw\_stock\_optimization`          | Optimization recommendations |

| `mart.vw\_executive\_kpi\_base`          | Executive KPI base           |



\---



\## 20. Business Metrics Supported



The platform supports the following business metrics:



\### Sales Metrics



\* Sales quantity

\* Gross sales amount

\* Discount amount

\* Net sales amount

\* VAT amount

\* Cost amount

\* Gross margin amount

\* Gross margin percentage



\### Inventory Metrics



\* Stock on hand

\* Available stock

\* Reserved stock

\* In-transit stock

\* On-order quantity

\* Inventory cost value

\* Inventory retail value

\* Stock cover days



\### Purchase Order Metrics



\* Ordered quantity

\* Cancelled quantity

\* Open quantity

\* Remaining quantity

\* Ordered cost value



\### Goods Receipt Metrics



\* Received quantity

\* Accepted quantity

\* Rejected quantity

\* Short quantity

\* Excess quantity

\* Defect quantity

\* Received cost value



\### Transfer Metrics



\* Requested transfer quantity

\* Shipped quantity

\* Received quantity

\* Short quantity

\* Excess quantity

\* In-transit quantity

\* Transfer cost value

\* Transfer retail value



\### Forecast Metrics



\* Forecast quantity

\* Actual quantity

\* Forecast error

\* Absolute error

\* Squared error

\* MAPE percentage

\* Bias percentage

\* Forecast accuracy percentage



\### Stock Optimization Metrics



\* Average daily sales

\* Demand standard deviation

\* Lead time days

\* Service level

\* Safety stock quantity

\* Reorder point quantity

\* Recommended order quantity

\* Stock cover days

\* Inventory health score



\---



\## 21. Portfolio Explanation



This project demonstrates the ability to design and build a full retail analytics platform from source files to reporting-ready data.



It includes:



\* Business problem understanding

\* Retail data modeling

\* SQL Server data warehouse design

\* Python ETL orchestration

\* Data validation

\* Audit logging

\* Error handling

\* File processing automation

\* Reporting outputs

\* Power BI-ready mart views

\* Command-line execution

\* Environment-based configuration



This is more than a dashboard project. It is a complete data engineering and analytics foundation for retail operations.



\---



\## 22. Interview Explanation



A concise interview explanation:



> I built an end-to-end Retail Intelligence Platform for fashion retail analytics. The project reads ERP-style Excel files, validates schema and data quality, loads clean data into SQL Server staging tables, executes stored procedures to populate a dimensional warehouse, and exposes mart views for Power BI. I also added audit tables, technical logs, Excel run summary reports, rejected row reports, processed/rejected file movement, environment configuration, and command-line controls. The platform supports sales, inventory, purchase orders, goods receipts, transfers, forecasting, and stock optimization analytics.



\---



\## 23. Future Enhancements



Planned next phases:



1\. Power BI executive dashboard

2\. Sales and inventory dashboard

3\. Purchase order and goods receipt dashboard

4\. Transfer and stock movement dashboard

5\. Forecast accuracy dashboard

6\. Forecast engine using Python

7\. Inventory optimization engine

8\. AI Supply Chain Assistant

9\. Flask web application

10\. Azure deployment

11\. GitHub publishing

12\. Final PDF project book



\---



\## 24. Current Progress



Current build completed:



```text

Build 26: Pipeline Run Summary Report

```



Next planned build:



```text

Build 27: Documentation and GitHub cleanup

```



\---



\## 25. Author



\*\*Kabir / Abrar Hussain\*\*

Inventory Controller

Retail, Supply Chain Analytics, Business Intelligence, and Data Warehouse Portfolio Project




