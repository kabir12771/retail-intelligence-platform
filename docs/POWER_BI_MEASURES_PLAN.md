\# Power BI Measures Plan



\## 1. Purpose



This document defines the planned Power BI measures for the Retail Intelligence Platform.



The measures will support executive reporting, sales analysis, inventory visibility, purchase order monitoring, transfer analysis, forecast accuracy, and stock optimization.



\---



\## 2. Sales Measures



```DAX

Total Sales Qty =

SUM ( vw\_sales\_performance\[sales\_qty] )

```



```DAX

Total Gross Sales =

SUM ( vw\_sales\_performance\[gross\_sales\_amount] )

```



```DAX

Total Discount =

SUM ( vw\_sales\_performance\[discount\_amount] )

```



```DAX

Total Net Sales =

SUM ( vw\_sales\_performance\[net\_sales\_amount] )

```



```DAX

Total VAT =

SUM ( vw\_sales\_performance\[vat\_amount] )

```



```DAX

Total Cost =

SUM ( vw\_sales\_performance\[cost\_amount] )

```



```DAX

Total Gross Margin =

SUM ( vw\_sales\_performance\[gross\_margin\_amount] )

```



```DAX

Gross Margin % =

DIVIDE ( \[Total Gross Margin], \[Total Net Sales], 0 )

```



\---



\## 3. Inventory Measures



```DAX

Stock On Hand Qty =

SUM ( vw\_inventory\_position\[stock\_on\_hand\_qty] )

```



```DAX

Available Qty =

SUM ( vw\_inventory\_position\[available\_qty] )

```



```DAX

Reserved Qty =

SUM ( vw\_inventory\_position\[reserved\_qty] )

```



```DAX

In Transit Qty =

SUM ( vw\_inventory\_position\[in\_transit\_qty] )

```



```DAX

On Order Qty =

SUM ( vw\_inventory\_position\[on\_order\_qty] )

```



```DAX

Inventory Cost Value =

SUM ( vw\_inventory\_position\[inventory\_cost\_value] )

```



```DAX

Inventory Retail Value =

SUM ( vw\_inventory\_position\[inventory\_retail\_value] )

```



```DAX

Average Stock Cover Days =

AVERAGE ( vw\_inventory\_position\[stock\_cover\_days] )

```



\---



\## 4. Purchase Order Measures



```DAX

Ordered Qty =

SUM ( vw\_purchase\_order\_analysis\[ordered\_qty] )

```



```DAX

Cancelled Qty =

SUM ( vw\_purchase\_order\_analysis\[cancelled\_qty] )

```



```DAX

Open Qty =

SUM ( vw\_purchase\_order\_analysis\[open\_qty] )

```



```DAX

Remaining Qty =

SUM ( vw\_purchase\_order\_analysis\[remaining\_qty] )

```



```DAX

Ordered Cost Value =

SUM ( vw\_purchase\_order\_analysis\[ordered\_cost\_value] )

```



```DAX

PO Fill Progress % =

DIVIDE ( \[Ordered Qty] - \[Remaining Qty], \[Ordered Qty], 0 )

```



\---



\## 5. Goods Receipt Measures



```DAX

Received Qty =

SUM ( vw\_goods\_receipt\_analysis\[received\_qty] )

```



```DAX

Accepted Qty =

SUM ( vw\_goods\_receipt\_analysis\[accepted\_qty] )

```



```DAX

Rejected Qty =

SUM ( vw\_goods\_receipt\_analysis\[rejected\_qty] )

```



```DAX

Short Qty =

SUM ( vw\_goods\_receipt\_analysis\[short\_qty] )

```



```DAX

Excess Qty =

SUM ( vw\_goods\_receipt\_analysis\[excess\_qty] )

```



```DAX

Defect Qty =

SUM ( vw\_goods\_receipt\_analysis\[defect\_qty] )

```



```DAX

Received Cost Value =

SUM ( vw\_goods\_receipt\_analysis\[received\_cost\_value] )

```



```DAX

Receipt Acceptance % =

DIVIDE ( \[Accepted Qty], \[Received Qty], 0 )

```



\---



\## 6. Transfer Measures



```DAX

Requested Transfer Qty =

SUM ( vw\_transfer\_analysis\[requested\_transfer\_qty] )

```



```DAX

Shipped Transfer Qty =

SUM ( vw\_transfer\_analysis\[shipped\_qty] )

```



```DAX

Received Transfer Qty =

SUM ( vw\_transfer\_analysis\[received\_qty] )

```



```DAX

Transfer Short Qty =

SUM ( vw\_transfer\_analysis\[short\_qty] )

```



```DAX

Transfer Excess Qty =

SUM ( vw\_transfer\_analysis\[excess\_qty] )

```



```DAX

Transfer In Transit Qty =

SUM ( vw\_transfer\_analysis\[in\_transit\_qty] )

```



```DAX

Transfer Cost Value =

SUM ( vw\_transfer\_analysis\[transfer\_cost\_value] )

```



```DAX

Transfer Completion % =

DIVIDE ( \[Received Transfer Qty], \[Shipped Transfer Qty], 0 )

```



\---



\## 7. Forecast Measures



```DAX

Forecast Qty =

SUM ( vw\_forecast\_accuracy\[forecast\_qty] )

```



```DAX

Actual Qty =

SUM ( vw\_forecast\_accuracy\[actual\_qty] )

```



```DAX

Forecast Error Qty =

SUM ( vw\_forecast\_accuracy\[forecast\_error\_qty] )

```



```DAX

Absolute Error Qty =

SUM ( vw\_forecast\_accuracy\[absolute\_error\_qty] )

```



```DAX

Squared Error Qty =

SUM ( vw\_forecast\_accuracy\[squared\_error\_qty] )

```



```DAX

WAPE % =

DIVIDE ( \[Absolute Error Qty], \[Actual Qty], 0 )

```



```DAX

Forecast Bias % =

DIVIDE ( \[Forecast Error Qty], \[Actual Qty], 0 )

```



```DAX

Forecast Accuracy % =

1 - \[WAPE %]

```



\---



\## 8. Stock Optimization Measures



```DAX

Average Daily Sales =

AVERAGE ( vw\_stock\_optimization\[avg\_daily\_sales] )

```



```DAX

Average Demand Std Dev =

AVERAGE ( vw\_stock\_optimization\[demand\_std\_dev] )

```



```DAX

Average Lead Time Days =

AVERAGE ( vw\_stock\_optimization\[lead\_time\_days] )

```



```DAX

Average Service Level =

AVERAGE ( vw\_stock\_optimization\[service\_level] )

```



```DAX

Safety Stock Qty =

SUM ( vw\_stock\_optimization\[safety\_stock\_qty] )

```



```DAX

Reorder Point Qty =

SUM ( vw\_stock\_optimization\[reorder\_point\_qty] )

```



```DAX

Recommended Order Qty =

SUM ( vw\_stock\_optimization\[recommended\_order\_qty] )

```



```DAX

Average Inventory Health Score =

AVERAGE ( vw\_stock\_optimization\[inventory\_health\_score] )

```



\---



\## 9. KPI Formatting Plan



Recommended formatting:



| Measure                | Format         |

| ---------------------- | -------------- |

| Quantity measures      | Whole number   |

| Sales value            | Currency       |

| Cost value             | Currency       |

| Margin percentage      | Percentage     |

| Forecast accuracy      | Percentage     |

| Forecast bias          | Percentage     |

| Stock cover days       | Decimal number |

| Inventory health score | Decimal number |



\---



\## 10. Dashboard Measure Priority



Create measures in this order:



1\. Sales measures

2\. Inventory measures

3\. Purchase order measures

4\. Goods receipt measures

5\. Transfer measures

6\. Forecast measures

7\. Stock optimization measures



This sequence matches the dashboard build order.



