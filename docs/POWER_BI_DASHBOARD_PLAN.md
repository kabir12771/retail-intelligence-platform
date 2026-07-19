\# Power BI Dashboard Plan



\## 1. Purpose



This document defines the Power BI dashboard plan for the Retail Intelligence Platform.



The goal is to convert SQL Server mart views into business-ready dashboards for retail leadership, inventory control, supply chain analytics, merchandise planning, and demand planning.



\---



\## 2. Dashboard Objective



The Power BI dashboard should help business users answer:



\* How are sales performing?

\* Which products, stores, and channels are driving revenue?

\* What is the current inventory position?

\* Where is stock overstocked or understocked?

\* Which purchase orders are still open?

\* Which goods receipts have shortages, excess, or rejected quantities?

\* Which transfers are pending, in-transit, or completed?

\* How accurate are forecasts?

\* Which products need replenishment or stock optimization action?



\---



\## 3. Data Source



Power BI will connect to SQL Server.



Database:



```text

RetailIntelligenceDW

```



Primary reporting schema:



```text

mart

```



Recommended connection mode:



```text

Import Mode

```



Import Mode is preferred for portfolio development because it is faster, easier to test, and works well with sample data.



\---



\## 4. Power BI Mart Views



The dashboard will use these SQL Server mart views:



| Mart View                             | Purpose                                        |

| ------------------------------------- | ---------------------------------------------- |

| `mart.vw\_executive\_kpi\_base`          | Executive KPI overview                         |

| `mart.vw\_sales\_performance`           | Sales and margin analysis                      |

| `mart.vw\_inventory\_position`          | Inventory stock position                       |

| `mart.vw\_latest\_inventory\_position`   | Latest stock snapshot                          |

| `mart.vw\_inventory\_movement\_analysis` | Stock movement analysis                        |

| `mart.vw\_purchase\_order\_analysis`     | Purchase order monitoring                      |

| `mart.vw\_goods\_receipt\_analysis`      | Goods receipt tracking                         |

| `mart.vw\_transfer\_analysis`           | Transfer tracking                              |

| `mart.vw\_forecast\_accuracy`           | Forecast performance                           |

| `mart.vw\_stock\_optimization`          | Replenishment and optimization recommendations |



\---



\## 5. Dashboard Pages



\### Page 1: Executive Overview



Purpose:



Provide a high-level summary of retail performance.



Recommended visuals:



\* KPI cards

\* Sales trend line chart

\* Inventory value card

\* Gross margin card

\* Forecast accuracy card

\* Inventory health score card

\* Top products table

\* Top locations table



Key metrics:



\* Net sales

\* Sales quantity

\* Gross margin

\* Gross margin percentage

\* Stock on hand

\* Inventory cost value

\* Forecast accuracy percentage

\* Inventory health score



Primary view:



```text

mart.vw\_executive\_kpi\_base

```



\---



\### Page 2: Sales Performance



Purpose:



Analyze sales by time, product, location, channel, and margin.



Recommended visuals:



\* Sales trend by date

\* Sales by product

\* Sales by location

\* Sales by channel

\* Gross margin by category

\* Top 10 products

\* Bottom 10 products

\* Product/location matrix



Primary view:



```text

mart.vw\_sales\_performance

```



Key questions:



\* Which products are selling best?

\* Which stores are generating the most sales?

\* Which channels are performing strongly?

\* Which products have low margin?



\---



\### Page 3: Inventory Position



Purpose:



Monitor stock availability, value, and coverage.



Recommended visuals:



\* Stock on hand card

\* Available stock card

\* Inventory value card

\* Stock cover days card

\* Inventory by location

\* Inventory by product category

\* Overstock/understock table

\* Latest inventory snapshot table



Primary views:



```text

mart.vw\_inventory\_position

mart.vw\_latest\_inventory\_position

```



Key questions:



\* Where is stock available?

\* Which stores have low stock?

\* Which products have high inventory value?

\* Which items may become stockout risks?



\---



\### Page 4: Purchase Orders and Goods Receipts



Purpose:



Track ordering, receiving, shortages, excess, and rejected quantities.



Recommended visuals:



\* Ordered quantity card

\* Open quantity card

\* Received quantity card

\* Short quantity card

\* PO status table

\* Supplier performance table

\* Goods receipt exception table

\* Expected vs received quantity chart



Primary views:



```text

mart.vw\_purchase\_order\_analysis

mart.vw\_goods\_receipt\_analysis

```



Key questions:



\* Which POs are still open?

\* Which suppliers have pending deliveries?

\* Which receipts had shortages?

\* Which receipts had rejected or defect quantities?



\---



\### Page 5: Transfers and Stock Movement



Purpose:



Track inter-store transfers and inventory movements.



Recommended visuals:



\* Transfer requested quantity card

\* Shipped quantity card

\* Received quantity card

\* In-transit quantity card

\* Transfer status table

\* Movement type breakdown

\* From-location to to-location transfer matrix

\* Stock movement trend



Primary views:



```text

mart.vw\_transfer\_analysis

mart.vw\_inventory\_movement\_analysis

```



Key questions:



\* Which transfers are in transit?

\* Which locations are sending or receiving stock?

\* Which movement types are most common?

\* Are there transfer shortages or excess quantities?



\---



\### Page 6: Forecast Accuracy



Purpose:



Evaluate forecast performance and demand planning quality.



Recommended visuals:



\* Forecast quantity card

\* Actual quantity card

\* Forecast accuracy card

\* MAPE card

\* Bias card

\* Forecast vs actual line chart

\* Forecast error by product

\* Forecast error by location



Primary view:



```text

mart.vw\_forecast\_accuracy

```



Key questions:



\* Is forecast accuracy improving?

\* Which products have poor forecast accuracy?

\* Which locations have high bias?

\* Is the forecast over-forecasting or under-forecasting?



\---



\### Page 7: Stock Optimization



Purpose:



Review replenishment and inventory optimization recommendations.



Recommended visuals:



\* Safety stock card

\* Reorder point card

\* Recommended order quantity card

\* Inventory health score card

\* ABC classification chart

\* XYZ classification chart

\* FSN classification chart

\* Recommended action table



Primary view:



```text

mart.vw\_stock\_optimization

```



Key questions:



\* Which products need reorder?

\* Which products are overstocked?

\* Which products are slow-moving?

\* Which items have weak inventory health?



\---



\## 6. Recommended Dashboard Style



Theme:



\* Clean executive style

\* Light background

\* Dark text

\* Retail/supply chain accent colors

\* Consistent KPI cards

\* Simple navigation

\* Minimal clutter



Recommended page structure:



```text

Top section: KPI cards

Middle section: Trend and breakdown visuals

Bottom section: detail tables and exceptions

```



\---



\## 7. Screenshot Plan



Dashboard screenshots should be saved in:



```text

screenshots

```



Recommended future screenshots:



```text

screenshots/executive\_overview.png

screenshots/sales\_performance.png

screenshots/inventory\_position.png

screenshots/po\_goods\_receipts.png

screenshots/transfers\_stock\_movement.png

screenshots/forecast\_accuracy.png

screenshots/stock\_optimization.png

```



These screenshots will later be added to README.



\---



\## 8. Build Sequence



Recommended dashboard build order:



1\. Executive Overview

2\. Sales Performance

3\. Inventory Position

4\. Purchase Orders and Goods Receipts

5\. Transfers and Stock Movement

6\. Forecast Accuracy

7\. Stock Optimization



\---



\## 9. Acceptance Criteria



The Power BI dashboard phase will be complete when:



\* Power BI connects to SQL Server successfully.

\* Mart views are imported.

\* Measures are created.

\* Executive Overview page is completed.

\* Sales Performance page is completed.

\* Inventory Position page is completed.

\* Operational pages are completed.

\* Forecast and optimization pages are completed.

\* Screenshots are added to GitHub.

\* README is updated with dashboard previews.



