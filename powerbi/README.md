\# Power BI Dashboard Layer



\## Purpose



This folder will contain Power BI-related project assets for the Retail Intelligence Platform.



The Power BI layer will connect to SQL Server mart views and convert the warehouse data into executive and operational dashboards.



\---



\## Planned Dashboard Pages



1\. Executive Overview

2\. Sales Performance

3\. Inventory Position

4\. Purchase Orders and Goods Receipts

5\. Transfers and Stock Movement

6\. Forecast Accuracy

7\. Stock Optimization



\---



\## Data Source



Database:



```text

RetailIntelligenceDW

```



Schema:



```text

mart

```



Recommended connection mode:



```text

Import Mode

```



\---



\## Primary Mart Views



\* `mart.vw\_executive\_kpi\_base`

\* `mart.vw\_sales\_performance`

\* `mart.vw\_inventory\_position`

\* `mart.vw\_latest\_inventory\_position`

\* `mart.vw\_inventory\_movement\_analysis`

\* `mart.vw\_purchase\_order\_analysis`

\* `mart.vw\_goods\_receipt\_analysis`

\* `mart.vw\_transfer\_analysis`

\* `mart.vw\_forecast\_accuracy`

\* `mart.vw\_stock\_optimization`



\---



\## Planned Power BI Assets



Future files may include:



```text

Retail\_Intelligence\_Platform.pbix

dashboard\_theme.json

measure\_documentation.md

dashboard\_screenshots

```



\---



\## Dashboard Screenshot Folder



Dashboard screenshots should be saved in:



```text

screenshots

```



Recommended image names:



```text

executive\_overview.png

sales\_performance.png

inventory\_position.png

po\_goods\_receipts.png

transfers\_stock\_movement.png

forecast\_accuracy.png

stock\_optimization.png

```



\---



\## Notes



The `.pbix` file may be added later after dashboard development starts.



Screenshots should be committed to GitHub to showcase the dashboard visually.



