\# Power BI DAX Measures Guide



\## 1. Purpose



This guide documents the DAX measures planned for the Executive Overview dashboard in the Retail Intelligence Platform.



The measures are stored in:



```text

powerbi/executive\_dashboard\_measures.dax

```



These measures are designed for the Power BI table:



```text

Executive KPI

```



The source SQL Server view is:



```text

mart.vw\_executive\_kpi\_base

```



\---



\## 2. Important Note



The `.dax` file is a reference file.



Power BI Desktop does not automatically import all measures from a `.dax` file by double-clicking it.



The correct approach is:



1\. Open Power BI Desktop.

2\. Load `mart.vw\_executive\_kpi\_base`.

3\. Rename the table to `Executive KPI`.

4\. Create each measure manually in Power BI.

5\. Copy each measure from `powerbi/executive\_dashboard\_measures.dax`.



\---



\## 3. Measure Groups



The Executive Dashboard measures are grouped into six areas:



| Group                       | Purpose                                                      |

| --------------------------- | ------------------------------------------------------------ |

| Sales Measures              | Net sales, quantity, margin, average selling price           |

| Inventory Measures          | Stock on hand, available stock, inventory value, stock cover |

| Forecast Measures           | Forecast quantity, actual quantity, WAPE, accuracy, bias     |

| Stock Optimization Measures | Safety stock, reorder point, recommended order quantity      |

| Executive KPI Measures      | Business summary ratios and high-level indicators            |

| Display Measures            | Dashboard title, subtitle, and refresh note                  |



\---



\## 4. Sales Measures



Sales measures support executive commercial performance reporting.



Main measures:



```text

Total Net Sales

Total Sales Qty

Total Gross Sales

Total Discount

Total VAT

Total Cost

Total Gross Margin

Gross Margin %

Average Selling Price

Average Cost Per Unit

```



Recommended visuals:



\* KPI cards

\* Sales trend line chart

\* Top products table

\* Location performance table

\* Gross margin analysis



\---



\## 5. Inventory Measures



Inventory measures support stock visibility and stock value reporting.



Main measures:



```text

Stock On Hand Qty

Available Qty

Reserved Qty

In Transit Qty

On Order Qty

Inventory Cost Value

Inventory Retail Value

Average Stock Cover Days

Inventory Sellable %

```



Recommended visuals:



\* Inventory value KPI card

\* Inventory by location bar chart

\* Stock on hand card

\* Available stock card

\* Stock cover card

\* Inventory exception table



\---



\## 6. Forecast Measures



Forecast measures support demand planning performance analysis.



Main measures:



```text

Forecast Qty

Actual Qty

Forecast Error Qty

Absolute Error Qty

WAPE %

Forecast Accuracy %

Forecast Bias %

Forecast Accuracy Status

```



Recommended visuals:



\* Forecast accuracy KPI card

\* Forecast vs actual chart

\* Forecast accuracy by product

\* Forecast bias table

\* Forecast exception list



\---



\## 7. Stock Optimization Measures



Stock optimization measures support replenishment and inventory action planning.



Main measures:



```text

Safety Stock Qty

Reorder Point Qty

Recommended Order Qty

Average Inventory Health Score

Inventory Health Status

```



Recommended visuals:



\* Inventory health score card

\* Recommended order quantity card

\* Replenishment table

\* ABC/XYZ/FSN classification charts

\* Stock action recommendations



\---



\## 8. Executive KPI Measures



Executive KPI measures provide leadership-level indicators.



Main measures:



```text

Total Business Value

Sales to Inventory Ratio

Gross Margin Per Unit

Inventory Risk Qty

Replenishment Need %

```



Recommended visuals:



\* Executive KPI cards

\* Business value card

\* Inventory risk card

\* Replenishment need indicator

\* KPI summary table



\---



\## 9. Display Measures



Display measures are optional but useful for dashboard polish.



Main measures:



```text

Executive Dashboard Title

Executive KPI Subtitle

Data Refresh Note

```



Recommended usage:



\* Page title

\* Subtitle

\* Footer note

\* Text card



\---



\## 10. Recommended Formatting



Use the following formatting in Power BI:



| Measure                        | Format         |

| ------------------------------ | -------------- |

| Total Net Sales                | Currency       |

| Total Gross Sales              | Currency       |

| Total Discount                 | Currency       |

| Total VAT                      | Currency       |

| Total Cost                     | Currency       |

| Total Gross Margin             | Currency       |

| Gross Margin %                 | Percentage     |

| Average Selling Price          | Currency       |

| Average Cost Per Unit          | Currency       |

| Stock On Hand Qty              | Whole number   |

| Available Qty                  | Whole number   |

| Reserved Qty                   | Whole number   |

| In Transit Qty                 | Whole number   |

| On Order Qty                   | Whole number   |

| Inventory Cost Value           | Currency       |

| Inventory Retail Value         | Currency       |

| Average Stock Cover Days       | Decimal number |

| Inventory Sellable %           | Percentage     |

| Forecast Qty                   | Whole number   |

| Actual Qty                     | Whole number   |

| WAPE %                         | Percentage     |

| Forecast Accuracy %            | Percentage     |

| Forecast Bias %                | Percentage     |

| Safety Stock Qty               | Whole number   |

| Reorder Point Qty              | Whole number   |

| Recommended Order Qty          | Whole number   |

| Average Inventory Health Score | Decimal number |

| Sales to Inventory Ratio       | Decimal number |

| Replenishment Need %           | Percentage     |



\---



\## 11. Dashboard KPI Card Priority



Use these measures first on the Executive Overview page:



1\. Total Net Sales

2\. Total Sales Qty

3\. Gross Margin %

4\. Inventory Cost Value

5\. Forecast Accuracy %

6\. Average Inventory Health Score



These six KPIs give the best executive summary.



\---



\## 12. Business Interpretation



\### Gross Margin %



Shows profitability after cost.



Strong explanation:



```text

Gross Margin % helps identify whether sales are profitable, not only whether sales volume is high.

```



\### Forecast Accuracy %



Shows demand planning quality.



Strong explanation:



```text

Forecast Accuracy % helps measure how close planned demand was to actual demand.

```



\### Inventory Health Score



Shows overall stock condition.



Strong explanation:



```text

Inventory Health Score summarizes whether stock levels are healthy, risky, overstocked, or understocked.

```



\### Recommended Order Qty



Shows replenishment need.



Strong explanation:



```text

Recommended Order Qty helps the business decide what quantity should be ordered based on demand, safety stock, and reorder logic.

```



\---



\## 13. Common Power BI Mistakes to Avoid



Avoid these issues:



\* Do not create calculated columns when a measure is more suitable.

\* Do not rename the table differently unless you also update all DAX formulas.

\* Do not use raw columns in KPI cards when a measure exists.

\* Do not format percentages as decimals.

\* Do not mix sales quantity with inventory quantity without clear labels.

\* Do not overload the executive page with too many visuals.



\---



\## 14. Acceptance Criteria



The DAX measures setup is complete when:



\* `powerbi/executive\_dashboard\_measures.dax` exists.

\* `docs/POWER\_BI\_DAX\_MEASURES\_GUIDE.md` exists.

\* Measures are grouped clearly.

\* Measures use the `Executive KPI` table name.

\* Measures are ready to copy into Power BI Desktop.

\* Documentation explains formatting and business meaning.



