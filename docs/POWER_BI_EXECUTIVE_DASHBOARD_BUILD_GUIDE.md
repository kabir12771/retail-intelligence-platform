\# Power BI Executive Dashboard Build Guide



\## 1. Purpose



This guide explains how to build the first Power BI page for the Retail Intelligence Platform.



Dashboard page:



```text

Executive Overview

```



The Executive Overview page is designed for leadership-level reporting. It should quickly show sales, inventory, margin, forecast, and stock optimization performance.



\---



\## 2. Dashboard Objective



The Executive Overview page should answer:



\* What is total sales performance?

\* What is the current inventory value?

\* What is the gross margin?

\* How accurate is the forecast?

\* How healthy is the inventory position?

\* Which products and locations need attention?



\---



\## 3. Data Source



Power BI will connect to SQL Server.



Database:



```text

RetailIntelligenceDW

```



Schema:



```text

mart

```



Primary view:



```text

mart.vw\_executive\_kpi\_base

```



Recommended connection mode:



```text

Import Mode

```



\---



\## 4. Connect Power BI to SQL Server



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



Select this view:



```text

mart.vw\_executive\_kpi\_base

```



Click:



```text

Load

```



\---



\## 5. Rename Table in Power BI



After loading the view, rename it in Power BI Fields pane.



From:



```text

vw\_executive\_kpi\_base

```



To:



```text

Executive KPI

```



This makes measure writing and dashboard design cleaner.



\---



\## 6. Recommended Page Setup



In Power BI Desktop:



Go to:



```text

Format Page → Canvas settings

```



Use:



```text

Type: 16:9

Width: 1280

Height: 720

```



Page name:



```text

Executive Overview

```



\---



\## 7. Dashboard Layout



Recommended layout:



```text

Top Row:

KPI Cards



Middle Row:

Sales trend + Inventory/Margin breakdown



Bottom Row:

Top products + Location performance + Exception table

```



Visual structure:



```text

\------------------------------------------------------------

| Title: Retail Intelligence Platform - Executive Overview |

\------------------------------------------------------------

| Net Sales | Sales Qty | Gross Margin % | Stock Value | Forecast Accuracy |

\------------------------------------------------------------

| Sales Trend by Date        | Inventory Value by Location |

\------------------------------------------------------------

| Top Products               | Location Performance        |

\------------------------------------------------------------

```



\---



\## 8. Core Measures



Create these measures in Power BI.



\### 8.1 Total Net Sales



```DAX

Total Net Sales =

SUM ( 'Executive KPI'\[net\_sales\_amount] )

```



\### 8.2 Total Sales Qty



```DAX

Total Sales Qty =

SUM ( 'Executive KPI'\[sales\_qty] )

```



\### 8.3 Total Gross Margin



```DAX

Total Gross Margin =

SUM ( 'Executive KPI'\[gross\_margin\_amount] )

```



\### 8.4 Gross Margin %



```DAX

Gross Margin % =

DIVIDE ( \[Total Gross Margin], \[Total Net Sales], 0 )

```



\### 8.5 Stock On Hand Qty



```DAX

Stock On Hand Qty =

SUM ( 'Executive KPI'\[stock\_on\_hand\_qty] )

```



\### 8.6 Inventory Cost Value



```DAX

Inventory Cost Value =

SUM ( 'Executive KPI'\[inventory\_cost\_value] )

```



\### 8.7 Inventory Retail Value



```DAX

Inventory Retail Value =

SUM ( 'Executive KPI'\[inventory\_retail\_value] )

```



\### 8.8 Forecast Qty



```DAX

Forecast Qty =

SUM ( 'Executive KPI'\[forecast\_qty] )

```



\### 8.9 Actual Qty



```DAX

Actual Qty =

SUM ( 'Executive KPI'\[actual\_qty] )

```



\### 8.10 Absolute Error Qty



```DAX

Absolute Error Qty =

SUM ( 'Executive KPI'\[absolute\_error\_qty] )

```



\### 8.11 WAPE %



```DAX

WAPE % =

DIVIDE ( \[Absolute Error Qty], \[Actual Qty], 0 )

```



\### 8.12 Forecast Accuracy %



```DAX

Forecast Accuracy % =

1 - \[WAPE %]

```



\### 8.13 Forecast Bias %



```DAX

Forecast Bias % =

DIVIDE ( \[Forecast Qty] - \[Actual Qty], \[Actual Qty], 0 )

```



\### 8.14 Recommended Order Qty



```DAX

Recommended Order Qty =

SUM ( 'Executive KPI'\[recommended\_order\_qty] )

```



\### 8.15 Average Inventory Health Score



```DAX

Average Inventory Health Score =

AVERAGE ( 'Executive KPI'\[inventory\_health\_score] )

```



\---



\## 9. KPI Card Visuals



Create 5 KPI cards at the top of the page.



\### Card 1: Net Sales



Measure:



```text

Total Net Sales

```



Format:



```text

Currency

```



Title:



```text

Net Sales

```



\---



\### Card 2: Sales Quantity



Measure:



```text

Total Sales Qty

```



Format:



```text

Whole number

```



Title:



```text

Sales Qty

```



\---



\### Card 3: Gross Margin %



Measure:



```text

Gross Margin %

```



Format:



```text

Percentage

```



Title:



```text

Gross Margin %

```



\---



\### Card 4: Inventory Cost Value



Measure:



```text

Inventory Cost Value

```



Format:



```text

Currency

```



Title:



```text

Inventory Value

```



\---



\### Card 5: Forecast Accuracy %



Measure:



```text

Forecast Accuracy %

```



Format:



```text

Percentage

```



Title:



```text

Forecast Accuracy

```



\---



\## 10. Sales Trend Visual



Visual type:



```text

Line chart

```



Fields:



```text

X-axis: transaction\_date or calendar\_date

Y-axis: Total Net Sales

```



Title:



```text

Net Sales Trend

```



Purpose:



Show sales movement over time.



\---



\## 11. Inventory Value by Location



Visual type:



```text

Bar chart

```



Fields:



```text

Y-axis: location\_name

X-axis: Inventory Cost Value

```



Sort:



```text

Inventory Cost Value descending

```



Title:



```text

Inventory Value by Location

```



Purpose:



Show where the highest inventory value is sitting.



\---



\## 12. Top Products Table



Visual type:



```text

Table

```



Fields:



```text

product\_code

product\_name

brand

category

Total Net Sales

Total Sales Qty

Total Gross Margin

Gross Margin %

```



Sort:



```text

Total Net Sales descending

```



Title:



```text

Top Products by Sales

```



Purpose:



Identify strongest selling products.



\---



\## 13. Location Performance Table



Visual type:



```text

Table

```



Fields:



```text

location\_code

location\_name

city

Total Net Sales

Total Sales Qty

Inventory Cost Value

Stock On Hand Qty

```



Sort:



```text

Total Net Sales descending

```



Title:



```text

Location Performance

```



Purpose:



Compare store or warehouse performance.



\---



\## 14. Inventory Health Visual



Visual type:



```text

Gauge or card

```



Measure:



```text

Average Inventory Health Score

```



Title:



```text

Inventory Health Score

```



Recommended interpretation:



```text

80 - 100 = Healthy

60 - 79  = Monitor

Below 60 = Action needed

```



\---



\## 15. Forecast Accuracy Visual



Visual type:



```text

Clustered column chart

```



Fields:



```text

X-axis: product\_code or category

Y-axis: Forecast Accuracy %

```



Title:



```text

Forecast Accuracy by Product

```



Purpose:



Identify products with weak forecast performance.



\---



\## 16. Recommended Filters / Slicers



Add slicers for:



```text

Date

Brand

Division

Department

Category

Season

Location

Channel

```



Use dropdown style for slicers to save space.



\---



\## 17. Formatting Rules



Recommended dashboard style:



```text

Background: light

Cards: white background

Borders: subtle grey

Titles: bold

Numbers: large and readable

Tables: compact

Use consistent spacing

```



Recommended card formatting:



```text

Callout value: large

Category label: on

Title: on

Background: on

Border: on

Shadow: light

```



Recommended number formatting:



| Measure             | Format       |

| ------------------- | ------------ |

| Net Sales           | Currency     |

| Inventory Value     | Currency     |

| Gross Margin %      | Percentage   |

| Forecast Accuracy % | Percentage   |

| Sales Qty           | Whole number |

| Stock Qty           | Whole number |



\---



\## 18. Suggested Color Meaning



Use colors consistently:



```text

Green: good / healthy / positive

Amber: warning / monitor

Red: risk / action needed

Blue: neutral business metric

Grey: secondary information

```



\---



\## 19. Dashboard Acceptance Criteria



The Executive Overview page is complete when:



\* SQL Server connection works.

\* `mart.vw\_executive\_kpi\_base` is loaded.

\* Core DAX measures are created.

\* Top KPI cards are visible.

\* Sales trend visual is created.

\* Inventory by location visual is created.

\* Top products table is created.

\* Location performance table is created.

\* Forecast accuracy visual is created.

\* Inventory health score visual is created.

\* Slicers are added.

\* Page is clean and readable.

\* Screenshot is exported.



\---



\## 20. Save Power BI File



Save the file as:



```text

powerbi/Retail\_Intelligence\_Platform.pbix

```



Note:



The `.pbix` file may become large. If GitHub file size becomes an issue, keep the `.pbix` local and commit only screenshots and documentation.



\---



\## 21. Export Screenshot



After completing the dashboard, export a screenshot as:



```text

screenshots/executive\_overview.png

```



This screenshot will later be added to README.



\---



\## 22. Recommended Build Order Inside Power BI



Build in this order:



1\. Connect to SQL Server.

2\. Load `mart.vw\_executive\_kpi\_base`.

3\. Rename table to `Executive KPI`.

4\. Create DAX measures.

5\. Add KPI cards.

6\. Add sales trend visual.

7\. Add inventory by location visual.

8\. Add top products table.

9\. Add location performance table.

10\. Add forecast accuracy visual.

11\. Add inventory health visual.

12\. Add slicers.

13\. Format layout.

14\. Save `.pbix`.

15\. Export screenshot.



\---



\## 23. Interview Explanation



A strong explanation for this dashboard:



```text

I built the Executive Overview page on top of SQL Server mart views. The dashboard summarizes key retail KPIs such as net sales, sales quantity, gross margin, inventory value, forecast accuracy, and inventory health. It helps leadership quickly understand commercial performance, inventory exposure, and planning quality from one page.

```



