\# Power BI Table Loading Checklist



\## 1. Connection



| Step                       | Status |

| -------------------------- | ------ |

| Open Power BI Desktop      | ☐      |

| Select Get Data            | ☐      |

| Select SQL Server          | ☐      |

| Enter server name          | ☐      |

| Enter database name        | ☐      |

| Select Import Mode         | ☐      |

| Use Windows Authentication | ☐      |

| Connect successfully       | ☐      |



Connection details:



```text

Server: localhost\\SQLEXPRESS

Database: RetailIntelligenceDW

Mode: Import

```



\---



\## 2. First Table Load



| Source View                  | Power BI Name   | Loaded |

| ---------------------------- | --------------- | ------ |

| `mart.vw\_executive\_kpi\_base` | `Executive KPI` | ☐      |



\---



\## 3. Full Mart View Load



| Source View                           | Power BI Name               | Loaded | Renamed | Data Types Checked |

| ------------------------------------- | --------------------------- | ------ | ------- | ------------------ |

| `mart.vw\_executive\_kpi\_base`          | `Executive KPI`             | ☐      | ☐       | ☐                  |

| `mart.vw\_sales\_performance`           | `Sales Performance`         | ☐      | ☐       | ☐                  |

| `mart.vw\_inventory\_position`          | `Inventory Position`        | ☐      | ☐       | ☐                  |

| `mart.vw\_latest\_inventory\_position`   | `Latest Inventory Position` | ☐      | ☐       | ☐                  |

| `mart.vw\_inventory\_movement\_analysis` | `Inventory Movement`        | ☐      | ☐       | ☐                  |

| `mart.vw\_purchase\_order\_analysis`     | `Purchase Orders`           | ☐      | ☐       | ☐                  |

| `mart.vw\_goods\_receipt\_analysis`      | `Goods Receipts`            | ☐      | ☐       | ☐                  |

| `mart.vw\_transfer\_analysis`           | `Transfers`                 | ☐      | ☐       | ☐                  |

| `mart.vw\_forecast\_accuracy`           | `Forecast Accuracy`         | ☐      | ☐       | ☐                  |

| `mart.vw\_stock\_optimization`          | `Stock Optimization`        | ☐      | ☐       | ☐                  |



\---



\## 4. Data Type Checks



| Data Type Area                              | Checked |

| ------------------------------------------- | ------- |

| Date columns are Date type                  | ☐       |

| Quantity columns are Whole Number           | ☐       |

| Amount columns are Decimal or Fixed Decimal | ☐       |

| Percentage columns are Decimal Number       | ☐       |

| Code columns are Text                       | ☐       |

| Status columns are Text                     | ☐       |

| Classification columns are Text             | ☐       |



\---



\## 5. Theme Import



| Step                                  | Status |

| ------------------------------------- | ------ |

| Open View tab                         | ☐      |

| Open Themes                           | ☐      |

| Browse for theme                      | ☐      |

| Select `powerbi/dashboard\_theme.json` | ☐      |

| Theme imported successfully           | ☐      |



\---



\## 6. Executive Dashboard Setup



| Step                                 | Status |

| ------------------------------------ | ------ |

| Page renamed to `Executive Overview` | ☐      |

| Table `Executive KPI` is available   | ☐      |

| Measures file opened                 | ☐      |

| Sales measures created               | ☐      |

| Inventory measures created           | ☐      |

| Forecast measures created            | ☐      |

| Optimization measures created        | ☐      |

| KPI cards added                      | ☐      |

| Main visuals added                   | ☐      |

| Slicers added                        | ☐      |

| Dashboard formatted                  | ☐      |

| Screenshot exported                  | ☐      |



\---



\## 7. Save File



Save the Power BI report as:



```text

powerbi/Retail\_Intelligence\_Platform.pbix

```



Checklist:



| Step                     | Status |

| ------------------------ | ------ |

| Power BI file saved      | ☐      |

| File name is correct     | ☐      |

| File location is correct | ☐      |

| Report refresh tested    | ☐      |



\---



\## 8. GitHub Screenshot Plan



After dashboard creation, export screenshots to:



```text

screenshots

```



Recommended first screenshot:



```text

screenshots/executive\_overview.png

```



Checklist:



| Step                           | Status |

| ------------------------------ | ------ |

| Screenshot exported            | ☐      |

| Screenshot saved as PNG        | ☐      |

| Screenshot added to README     | ☐      |

| Screenshot committed to GitHub | ☐      |



