\# Power BI Data Connection and Table Loading Guide



\## 1. Purpose



This guide explains how to connect Power BI Desktop to the Retail Intelligence Platform SQL Server database and load the required reporting views.



The goal is to prepare a clean Power BI model before dashboard development starts.



\---



\## 2. Source System



Power BI will connect to:



```text

SQL Server

```



Database:



```text

RetailIntelligenceDW

```



Main reporting schema:



```text

mart

```



Recommended mode:



```text

Import Mode

```



Import Mode is recommended for the portfolio version because it is fast, easy to refresh, and works well with sample/demo data.



\---



\## 3. SQL Server Connection Steps



Open Power BI Desktop.



Go to:



```text

Home → Get Data → SQL Server

```



Enter:



```text

Server: localhost\\SQLEXPRESS

Database: RetailIntelligenceDW

```



Choose:



```text

Data Connectivity Mode: Import

```



Then click:



```text

OK

```



Authentication:



```text

Windows Authentication

```



Then click:



```text

Connect

```



\---



\## 4. Required Mart Views



Load these views from the `mart` schema:



| Source View                           | Power BI Table Name         | Purpose                        |

| ------------------------------------- | --------------------------- | ------------------------------ |

| `mart.vw\_executive\_kpi\_base`          | `Executive KPI`             | Executive overview             |

| `mart.vw\_sales\_performance`           | `Sales Performance`         | Sales and margin dashboard     |

| `mart.vw\_inventory\_position`          | `Inventory Position`        | Inventory stock analysis       |

| `mart.vw\_latest\_inventory\_position`   | `Latest Inventory Position` | Latest stock snapshot          |

| `mart.vw\_inventory\_movement\_analysis` | `Inventory Movement`        | Stock movement analysis        |

| `mart.vw\_purchase\_order\_analysis`     | `Purchase Orders`           | Purchase order tracking        |

| `mart.vw\_goods\_receipt\_analysis`      | `Goods Receipts`            | Receiving and GRN analysis     |

| `mart.vw\_transfer\_analysis`           | `Transfers`                 | Inter-store transfer tracking  |

| `mart.vw\_forecast\_accuracy`           | `Forecast Accuracy`         | Forecast performance           |

| `mart.vw\_stock\_optimization`          | `Stock Optimization`        | Replenishment and optimization |



\---



\## 5. Recommended First Load



For the first Power BI test, load only:



```text

mart.vw\_executive\_kpi\_base

```



Rename it to:



```text

Executive KPI

```



This allows the Executive Overview dashboard to be built first without overloading the model.



After the Executive Overview page works, load the remaining mart views.



\---



\## 6. Full Load Sequence



Recommended loading order:



1\. `mart.vw\_executive\_kpi\_base`

2\. `mart.vw\_sales\_performance`

3\. `mart.vw\_inventory\_position`

4\. `mart.vw\_latest\_inventory\_position`

5\. `mart.vw\_inventory\_movement\_analysis`

6\. `mart.vw\_purchase\_order\_analysis`

7\. `mart.vw\_goods\_receipt\_analysis`

8\. `mart.vw\_transfer\_analysis`

9\. `mart.vw\_forecast\_accuracy`

10\. `mart.vw\_stock\_optimization`



\---



\## 7. Table Naming Standard



After loading each view, rename the Power BI table.



Use business-friendly table names:



```text

Executive KPI

Sales Performance

Inventory Position

Latest Inventory Position

Inventory Movement

Purchase Orders

Goods Receipts

Transfers

Forecast Accuracy

Stock Optimization

```



Avoid technical names like:



```text

vw\_executive\_kpi\_base

vw\_sales\_performance

vw\_inventory\_position

```



Business-friendly names make DAX measures and dashboard development easier.



\---



\## 8. Data Type Checklist



After loading the views, open Power Query and verify data types.



Recommended data types:



| Column Type            | Power BI Data Type                     |

| ---------------------- | -------------------------------------- |

| Date columns           | Date                                   |

| DateTime columns       | Date/Time                              |

| Product code           | Text                                   |

| Location code          | Text                                   |

| Supplier code          | Text                                   |

| Barcode                | Text                                   |

| Quantity columns       | Whole Number                           |

| Amount columns         | Decimal Number or Fixed Decimal Number |

| Percentage columns     | Decimal Number                         |

| Status columns         | Text                                   |

| Classification columns | Text                                   |



\---



\## 9. Common Date Columns



Check these columns where available:



```text

transaction\_date

snapshot\_date

movement\_date

order\_date

expected\_receipt\_date

receipt\_date

transfer\_date

ship\_date

receive\_date

forecast\_date

optimization\_date

calendar\_date

```



Set them as:



```text

Date

```



\---



\## 10. Common Quantity Columns



Check these columns where available:



```text

sales\_qty

stock\_on\_hand\_qty

available\_qty

reserved\_qty

in\_transit\_qty

on\_order\_qty

ordered\_qty

received\_qty

accepted\_qty

rejected\_qty

short\_qty

excess\_qty

defect\_qty

forecast\_qty

actual\_qty

safety\_stock\_qty

reorder\_point\_qty

recommended\_order\_qty

```



Set them as:



```text

Whole Number

```



\---



\## 11. Common Amount Columns



Check these columns where available:



```text

gross\_sales\_amount

discount\_amount

net\_sales\_amount

vat\_amount

cost\_amount

gross\_margin\_amount

inventory\_cost\_value

inventory\_retail\_value

ordered\_cost\_value

received\_cost\_value

transfer\_cost\_value

```



Set them as:



```text

Decimal Number

```



or:



```text

Fixed Decimal Number

```



Use currency formatting later in Power BI Model view.



\---



\## 12. Common Percentage Columns



Check these columns where available:



```text

gross\_margin\_percentage

forecast\_accuracy\_percentage

bias\_percentage

mape\_percentage

wape\_percentage

service\_level

```



Set them as:



```text

Decimal Number

```



Then format them as:



```text

Percentage

```



\---



\## 13. Model Relationship Recommendation



For the first portfolio version, each dashboard page can use its own mart view.



Recommended approach:



```text

Use mart views as reporting-ready wide tables.

Build measures on top of each mart view.

Avoid unnecessary relationships in the first version.

```



Reason:



The SQL Server mart views already combine the required fact and dimension information for reporting.



This keeps the Power BI model simple and easy to explain.



\---



\## 14. Future Advanced Model



A future advanced version may import dimension tables and fact tables separately.



Possible future model:



```text

dim\_product

dim\_location

dim\_calendar

dim\_channel

dim\_supplier

fact\_sales

fact\_inventory\_snapshot

fact\_purchase\_orders

fact\_goods\_receipts

fact\_transfers

fact\_forecast

fact\_stock\_optimization

```



This would create a full star schema inside Power BI.



For the first dashboard version, mart views are enough.



\---



\## 15. Refresh Steps



To refresh the report:



Go to:



```text

Home → Refresh

```



Power BI will reload the data from SQL Server.



Before refreshing, make sure:



```text

SQL Server is running

RetailIntelligenceDW database exists

ETL pipeline has been executed

Mart views are available

```



\---



\## 16. SQL Validation Before Power BI Load



Before connecting Power BI, run these checks in SQL Server Management Studio:



```sql

SELECT COUNT(\*) AS row\_count FROM mart.vw\_executive\_kpi\_base;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_sales\_performance;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_inventory\_position;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_latest\_inventory\_position;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_inventory\_movement\_analysis;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_purchase\_order\_analysis;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_goods\_receipt\_analysis;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_transfer\_analysis;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_forecast\_accuracy;

SELECT COUNT(\*) AS row\_count FROM mart.vw\_stock\_optimization;

```



Each view should return rows.



\---



\## 17. Power BI Save Location



Save the Power BI file as:



```text

powerbi/Retail\_Intelligence\_Platform.pbix

```



If GitHub file size becomes an issue, keep the `.pbix` file local and upload only documentation and screenshots.



\---



\## 18. Recommended First Dashboard Page



Start with:



```text

Executive Overview

```



Primary table:



```text

Executive KPI

```



Required measure file:



```text

powerbi/executive\_dashboard\_measures.dax

```



Theme file:



```text

powerbi/dashboard\_theme.json

```



\---



\## 19. Acceptance Criteria



The Power BI connection setup is complete when:



\* Power BI connects to SQL Server successfully.

\* `RetailIntelligenceDW` database is selected.

\* `mart.vw\_executive\_kpi\_base` is loaded.

\* Table is renamed to `Executive KPI`.

\* Required data types are checked.

\* Dashboard theme is imported.

\* DAX measures are ready to create.

\* Power BI file is saved in the `powerbi` folder.



