\# Power BI Theme Guide



\## 1. Purpose



This document explains the Power BI dashboard theme used in the Retail Intelligence Platform.



Theme file:



```text id="1k9e1o"

powerbi/dashboard\_theme.json

```



The theme is designed for a clean executive retail analytics dashboard.



\---



\## 2. Theme Name



```text id="bjklru"

Retail Intelligence Executive Theme

```



\---



\## 3. Design Direction



The dashboard design should feel:



\* Professional

\* Clean

\* Executive-ready

\* Retail-focused

\* Easy to read

\* Suitable for GitHub portfolio screenshots



\---



\## 4. Main Colors



| Purpose           | Color     |

| ----------------- | --------- |

| Primary blue      | `#2563EB` |

| Good / positive   | `#10B981` |

| Warning / monitor | `#F59E0B` |

| Bad / risk        | `#EF4444` |

| Purple accent     | `#8B5CF6` |

| Cyan accent       | `#06B6D4` |

| Background        | `#F8FAFC` |

| Card background   | `#FFFFFF` |

| Main text         | `#111827` |

| Secondary text    | `#475569` |

| Border            | `#E5E7EB` |



\---



\## 5. Color Meaning



Use colors consistently:



```text id="nlfa4a"

Blue   = neutral business metric

Green  = good / healthy / positive

Amber  = warning / monitor

Red    = risk / action needed

Grey   = secondary information

```



Examples:



| KPI                    | Suggested Color Logic                            |

| ---------------------- | ------------------------------------------------ |

| Forecast Accuracy      | Green when high, amber when medium, red when low |

| Inventory Health Score | Green above 80, amber 60-79, red below 60        |

| Stockout Risk          | Red for high risk                                |

| Overstock              | Amber or red depending on severity               |

| Gross Margin %         | Green when healthy                               |



\---



\## 6. Font Plan



Recommended font:



```text id="pmd2sb"

Segoe UI

```



Recommended usage:



| Text Type    | Font              |

| ------------ | ----------------- |

| Page title   | Segoe UI Semibold |

| Visual title | Segoe UI Semibold |

| KPI value    | Segoe UI Semibold |

| Table value  | Segoe UI          |

| Slicer value | Segoe UI          |



\---



\## 7. Import Theme in Power BI



Open Power BI Desktop.



Go to:



```text id="h1evxt"

View → Themes → Browse for themes

```



Select:



```text id="3qfjwr"

powerbi/dashboard\_theme.json

```



Click:



```text id="wptnyn"

Open

```



Power BI should apply the theme to the report.



\---



\## 8. Recommended Page Style



Use this page setup:



```text id="bwgmuf"

Canvas size: 16:9

Background: #F8FAFC

Cards: white

Borders: light grey

Spacing: consistent

Titles: short and clear

```



Recommended layout:



```text id="tuqw7j"

Top: KPI cards

Middle: trends and breakdowns

Bottom: tables and exception details

```



\---



\## 9. KPI Card Style



Recommended card design:



```text id="7ckpgq"

White background

Rounded border

Light shadow

Large value

Small label

No unnecessary icons

```



Good KPI card examples:



```text id="chjivv"

Net Sales

Sales Qty

Gross Margin %

Inventory Value

Forecast Accuracy

Inventory Health Score

```



\---



\## 10. Table Style



Recommended table design:



```text id="ui7n31"

Compact row height

Light header background

No heavy grid lines

Important numbers right aligned

Text fields left aligned

Sorted by most important metric

```



Use tables for:



```text id="r9jn23"

Top Products

Location Performance

PO Exceptions

Goods Receipt Exceptions

Transfer Exceptions

Forecast Accuracy Exceptions

Optimization Recommendations

```



\---



\## 11. Visual Style



Recommended visuals:



| Dashboard Area               | Visual Type        |

| ---------------------------- | ------------------ |

| KPI summary                  | Card               |

| Sales trend                  | Line chart         |

| Inventory by location        | Bar chart          |

| Forecast vs actual           | Line chart         |

| Forecast accuracy by product | Column chart       |

| ABC / XYZ / FSN              | Donut or bar chart |

| Exceptions                   | Table              |



\---



\## 12. Screenshot Standard



When exporting screenshots for GitHub:



```text id="n6a1um"

Use full-screen dashboard view

Hide Power BI side panes

Use clean filters

Avoid random test selections

Make sure KPI cards are readable

Save screenshots as PNG

```



Recommended screenshot location:



```text id="516sb7"

screenshots

```



Recommended file names:



```text id="v37ddl"

executive\_overview.png

sales\_performance.png

inventory\_position.png

po\_goods\_receipts.png

transfers\_stock\_movement.png

forecast\_accuracy.png

stock\_optimization.png

```



\---



\## 13. Portfolio Explanation



A strong interview explanation:



```text id="ne7kk7"

I created a custom Power BI theme to keep the dashboard visually consistent across all pages. The theme uses an executive-style layout with clean cards, subtle borders, readable typography, and consistent color meanings for positive, warning, and risk indicators.

```



\---



\## 14. Acceptance Criteria



The theme setup is complete when:



\* `dashboard\_theme.json` exists in the `powerbi` folder.

\* The theme imports successfully into Power BI Desktop.

\* Dashboard visuals use consistent fonts and colors.

\* KPI cards follow the executive dashboard style.

\* Tables and slicers are clean and readable.

\* Screenshot output looks professional.



