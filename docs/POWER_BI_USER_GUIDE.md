# Power BI User Guide  
# Retail Intelligence Platform

## 1. Purpose

This document explains how to use, refresh, maintain, and present the Power BI dashboard layer of the Retail Intelligence Platform.

The Power BI report is built on top of SQL Server mart views created by the Python ETL and SQL Server data warehouse pipeline.

The dashboard supports retail business analysis across:

- Executive performance
- Sales performance
- Inventory position
- Forecast accuracy
- Stock optimization
- Purchase order control
- Goods receipt analysis
- Transfer operations
- Inventory movement monitoring

---

## 2. Power BI File

Main Power BI report file:

```text
powerbi/Retail_Intelligence_Platform.pbix
```

Dashboard screenshots are stored in:

```text
screenshots/
```

Power BI theme file:

```text
powerbi/dashboard_theme.json
```

DAX measure files:

```text
powerbi/executive_dashboard_measures.dax
powerbi/forecast_accuracy_advanced_measures.dax
powerbi/stock_optimization_additional_measures.dax
```

---

## 3. Data Source

Power BI connects to SQL Server.

Default connection used in this project:

```text
Server: localhost\SQLEXPRESS
Database: RetailIntelligenceDW
Connection Mode: Import
```

The dashboard uses reporting views from the SQL Server `mart` schema.

---

## 4. Power BI Data Model Approach

For this portfolio version, the Power BI model uses standalone reporting mart views.

Important rule:

```text
One dashboard page = one mart view
One mart view = one standalone reporting table
Do not create relationships between mart views
Do not mix fields from different mart tables in the same visual
```

This approach is used because mart views already contain descriptive reporting fields such as:

- brand
- department
- category
- product_name
- location_name
- date fields
- KPI columns

These fields are repeated naturally and should be used as slicers or visual fields, not primary keys.

---

## 5. Relationship Rule

For this version, relationships between reporting tables should be removed.

Power BI should not create automatic relationships using fields such as:

```text
brand
department
category
product_name
location_name
net_sales_amount
stock_on_hand_qty
inventory_cost_value
```

These columns are not unique. They are descriptive reporting columns.

Recommended Power BI setting:

```text
File → Options and settings → Options → Current File → Data Load
```

Disable:

```text
Autodetect new relationships after data is loaded
Import relationships from data sources on first load
Update or delete relationships when refreshing data
Auto date/time
```

---

## 6. Reporting Tables

| Power BI Table | SQL Server Mart View | Usage |
|---|---|---|
| Executive KPI | `mart.vw_executive_kpi_base` | Executive overview page |
| Sales Performance | `mart.vw_sales_performance` | Sales performance page |
| Inventory Position | `mart.vw_inventory_position` | Inventory analysis |
| Latest Inventory Position | `mart.vw_latest_inventory_position` | Latest stock snapshot |
| Forecast Accuracy | `mart.vw_forecast_accuracy` | Forecast vs actual analysis |
| Stock Optimization | `mart.vw_stock_optimization` | Reorder and inventory health |
| Purchase Orders | `mart.vw_purchase_order_analysis` | Purchase order monitoring |
| Goods Receipts | `mart.vw_goods_receipt_analysis` | Receiving and GRN analysis |
| Transfers | `mart.vw_transfer_analysis` | Transfer tracking |
| Inventory Movement | `mart.vw_inventory_movement_analysis` | Stock movement analysis |

---

## 7. Dashboard Pages

## 7.1 Executive Overview

Main table:

```text
Executive KPI
```

Purpose:

The Executive Overview page provides a high-level view of total retail business performance.

Focus areas:

- Net sales
- Units sold
- Gross margin
- Gross margin percentage
- Inventory value
- Stock cover
- Business health indicators

Recommended users:

- Senior management
- Retail operations managers
- Merchandise planners
- Demand planners
- Inventory controllers

Screenshot:

```text
screenshots/executive_overview.png
```

Important rule:

Use only fields from the `Executive KPI` table on this page.

---

## 7.2 Sales Performance

Main table:

```text
Sales Performance
```

Purpose:

The Sales Performance page explains how revenue, quantity, and margin are performing across stores, brands, departments, categories, and products.

Focus areas:

- Net sales
- Sales quantity
- Gross margin
- Gross margin percentage
- Category contribution
- Product contribution
- Store/location performance

Screenshot:

```text
screenshots/sales_performance.png
```

Important rule:

Use only fields from the `Sales Performance` table on this page.

---

## 7.3 Forecast Accuracy

Main table:

```text
Forecast Accuracy
```

Purpose:

The Forecast Accuracy page compares forecast demand against actual sales and highlights planning exceptions.

Focus areas:

- Forecast quantity
- Actual quantity
- Forecast error
- Absolute error
- WAPE percentage
- Forecast accuracy percentage
- Forecast bias percentage
- Over-forecast and under-forecast cases

Screenshot:

```text
screenshots/forecast_accuracy.png
```

Important rule:

Use only fields from the `Forecast Accuracy` table on this page.

Do not use date, product, location, brand, or category fields from other tables.

Correct example:

```text
Axis: Forecast Accuracy[product_name]
Value: Forecast Accuracy[Forecast Accuracy %]
```

Wrong example:

```text
Axis: Sales Performance[product_name]
Value: Forecast Accuracy[Forecast Accuracy %]
```

---

## 7.4 Stock Optimization

Main table:

```text
Stock Optimization
```

Purpose:

The Stock Optimization page supports replenishment and inventory control decisions.

Focus areas:

- Inventory health score
- Safety stock quantity
- Reorder point quantity
- Recommended order quantity
- Average daily sales
- Lead time days
- Stock cover days
- ABC classification
- XYZ classification
- FSN classification
- Replenishment recommendation

Screenshot:

```text
screenshots/stock_optimization.png
```

Important rule:

Use only fields from the `Stock Optimization` table on this page.

---

## 7.5 Inventory Position

Main tables:

```text
Inventory Position
Latest Inventory Position
```

Purpose:

The Inventory Position page monitors current and historical stock position.

Focus areas:

- Stock on hand
- Available stock
- Reserved stock
- In-transit stock
- On-order quantity
- Inventory cost value
- Inventory retail value
- Stock cover days

Important rule:

Use `Inventory Position` fields for historical inventory visuals.

Use `Latest Inventory Position` fields for latest snapshot KPI cards.

Do not mix fields from unrelated mart tables in the same visual.

---

## 7.6 Operations Control

Main tables:

```text
Purchase Orders
Goods Receipts
Transfers
Inventory Movement
```

Purpose:

The Operations Control page tracks supply chain execution across purchasing, receiving, transfers, and stock movements.

Important rule:

Do not mix fields from different operation tables in the same visual.

Use:

```text
PO visuals → Purchase Orders table
GRN visuals → Goods Receipts table
Transfer visuals → Transfers table
Movement visuals → Inventory Movement table
```

Focus areas:

- Ordered quantity
- Remaining quantity
- Received quantity
- Accepted quantity
- Rejected quantity
- Transfer shipped quantity
- Transfer received quantity
- In-transit quantity
- Inventory movement quantity

---

## 8. KPI Definitions

## 8.1 Sales KPIs

| KPI | Meaning |
|---|---|
| Net Sales | Sales after discount |
| Gross Sales | Sales before discount |
| Sales Quantity | Units sold |
| Gross Margin | Net sales minus cost |
| Gross Margin % | Gross margin divided by net sales |
| Average Selling Price | Net sales divided by quantity sold |

---

## 8.2 Inventory KPIs

| KPI | Meaning |
|---|---|
| Stock on Hand | Total physical stock |
| Available Stock | Sellable stock available |
| Reserved Stock | Stock reserved for orders or operations |
| In-Transit Stock | Stock moving between locations |
| On-Order Quantity | Quantity ordered but not yet received |
| Inventory Cost Value | Stock quantity multiplied by unit cost |
| Inventory Retail Value | Stock quantity multiplied by retail price |
| Stock Cover Days | Estimated number of days stock can support demand |

---

## 8.3 Forecast KPIs

| KPI | Formula / Meaning |
|---|---|
| Forecast Qty | Planned demand |
| Actual Qty | Real demand / actual sales |
| Forecast Error | Actual Qty - Forecast Qty |
| Absolute Error | Absolute value of forecast error |
| WAPE % | Absolute Error Qty / Actual Qty |
| Forecast Accuracy % | 1 - WAPE % |
| Forecast Bias % | Forecast Error Qty / Actual Qty |

Forecast accuracy rule:

```text
Green  = Forecast Accuracy >= 85%
Amber  = Forecast Accuracy between 70% and 84.99%
Red    = Forecast Accuracy below 70%
```

Bias interpretation:

```text
Positive Bias = Actual higher than forecast = Under forecast
Negative Bias = Actual lower than forecast = Over forecast
```

---

## 8.4 Stock Optimization KPIs

| KPI | Meaning |
|---|---|
| Average Daily Sales | Average item demand per day |
| Demand Std Dev | Demand variability |
| Lead Time Days | Supplier or replenishment lead time |
| Service Level | Target service availability |
| Safety Stock Qty | Buffer stock to protect against demand/lead time variation |
| Reorder Point Qty | Stock level where replenishment should start |
| Recommended Order Qty | Suggested replenishment quantity |
| Stock Cover Days | Days of supply available |
| Inventory Health Score | Overall inventory risk/health indicator |
| ABC Class | Value or importance classification |
| XYZ Class | Demand variability classification |
| FSN Class | Fast, slow, non-moving classification |

Inventory health rule:

```text
Green  = Inventory Health Score >= 80
Amber  = Inventory Health Score between 60 and 79.99
Red    = Inventory Health Score below 60
```

---

## 9. Recommended Slicers

Use slicers from the same table as the page.

Common slicers:

- brand
- department
- category
- season
- product_name
- location_name
- recommendation
- abc_class
- xyz_class
- fsn_class

Do not use slicers from another table unless a valid relationship model exists.

---

## 10. Conditional Formatting Rules

## 10.1 Forecast Accuracy

```text
Green  = >= 85%
Amber  = 70% to 84.99%
Red    = below 70%
```

DAX color measure example:

```DAX
Forecast Accuracy Color =
SWITCH (
    TRUE (),
    [Forecast Accuracy %] >= 0.85, "#16A34A",
    [Forecast Accuracy %] >= 0.70, "#F59E0B",
    "#DC2626"
)
```

---

## 10.2 WAPE

```text
Green  = <= 15%
Amber  = 15% to 30%
Red    = above 30%
```

---

## 10.3 Forecast Bias

```text
Green  = between -10% and +10%
Amber  = between -20% and +20%
Red    = outside +/-20%
```

---

## 10.4 Inventory Health Score

```text
Green  = >= 80
Amber  = 60 to 79.99
Red    = below 60
```

DAX color measure example:

```DAX
Inventory Health Color =
SWITCH (
    TRUE (),
    [Average Inventory Health Score] >= 80, "#16A34A",
    [Average Inventory Health Score] >= 60, "#F59E0B",
    "#DC2626"
)
```

---

## 11. Refresh Process

Before refreshing Power BI:

1. Run the Python ETL pipeline.
2. Confirm SQL Server mart views have data.
3. Open Power BI Desktop.
4. Disable auto relationships if not already disabled.
5. Click Refresh.
6. Confirm all tables load successfully.
7. Save the PBIX file.
8. Export updated screenshots if dashboard layout changed.

Refresh command in Power BI:

```text
Home → Refresh
```

---

## 12. SQL Validation Queries

Check forecast and optimization row counts:

```sql
USE RetailIntelligenceDW;
GO

SELECT 'dw.fact_forecast' AS table_name, COUNT(*) AS row_count
FROM dw.fact_forecast

UNION ALL

SELECT 'mart.vw_forecast_accuracy' AS table_name, COUNT(*) AS row_count
FROM mart.vw_forecast_accuracy

UNION ALL

SELECT 'dw.fact_stock_optimization' AS table_name, COUNT(*) AS row_count
FROM dw.fact_stock_optimization

UNION ALL

SELECT 'mart.vw_stock_optimization' AS table_name, COUNT(*) AS row_count
FROM mart.vw_stock_optimization;
```

Expected demo data after expansion:

```text
dw.fact_forecast              393
mart.vw_forecast_accuracy     393
dw.fact_stock_optimization    18
mart.vw_stock_optimization    18
```

---

## 13. Troubleshooting

## 13.1 Duplicate Value Relationship Error

Example error:

```text
Column 'department' in Table 'Stock Optimization' contains a duplicate value and this is not allowed for columns on the one side of a many-to-one relationship.
```

Cause:

Power BI created an incorrect relationship using a repeated descriptive field.

Fix:

1. Go to Model View.
2. Open Manage Relationships.
3. Delete relationships between mart views.
4. Disable auto relationship detection.
5. Refresh again.

---

## 13.2 OLE DB or ODBC Error

Cause may be:

- Previous table load failed
- SQL Server connection issue
- Broken query step
- Wrong table/view name
- Relationship error cascading into other table refresh failures

Fix:

1. Check the first table that failed.
2. Fix that table first.
3. Delete wrong relationships.
4. Refresh again.
5. If needed, delete and reload the broken query from SQL Server.

---

## 13.3 Missing Column Error

Cause:

A DAX measure or visual references a column that does not exist in the selected table.

Fix:

1. Open Fields pane.
2. Confirm exact column name.
3. Edit the measure or visual.
4. Use fields only from the page's main table.

---

## 13.4 Visual Not Filtering Correctly

Cause:

The visual is using fields from different standalone mart tables.

Fix:

Use fields and measures from the same table in the visual.

Correct example:

```text
Axis: Forecast Accuracy[product_name]
Value: Forecast Accuracy[Forecast Accuracy %]
```

Wrong example:

```text
Axis: Sales Performance[product_name]
Value: Forecast Accuracy[Forecast Accuracy %]
```

---

## 14. GitHub Screenshot Update Process

When a dashboard page is updated:

1. Save PBIX.
2. Export screenshot.
3. Save screenshot in the `screenshots` folder.
4. Commit PBIX and screenshot.

Example:

```powershell
git status --short
git add powerbi\Retail_Intelligence_Platform.pbix
git add screenshots\forecast_accuracy.png
git commit -m "Update forecast accuracy Power BI dashboard"
git push
git status
```

---

## 15. Portfolio Presentation Script

Use this explanation when presenting the Power BI layer:

> The Power BI dashboard connects to SQL Server mart views created by my Python ETL and data warehouse pipeline. Each dashboard page uses a standalone analytics-ready mart table, which avoids incorrect relationships between repeated descriptive fields such as brand, department, category, and product name. The dashboard includes executive KPIs, sales performance, inventory position, forecast accuracy, stock optimization, and operations control. I also created DAX measures, conditional formatting, dashboard screenshots, and documentation so the project is ready for GitHub portfolio and interview presentation.

---

## 16. User Guide Summary

The Power BI layer is designed to be:

- Business-friendly
- Fast to refresh
- Easy to maintain
- Clear for portfolio presentation
- Connected to SQL Server mart views
- Supported by DAX measure files
- Documented for future improvement

The current version is a professional portfolio-ready dashboard layer.

A future advanced version can use a full star-schema Power BI model with dimension tables and relationship-based cross-page filtering.