\# GitHub Issues Plan



\## Purpose



This document defines the planned GitHub issue structure for the Retail Intelligence Platform.



The goal is to manage future work professionally using GitHub Issues, labels, and milestones.



\---



\## Suggested GitHub Labels



\### Type Labels



| Label               | Purpose                         |

| ------------------- | ------------------------------- |

| type: feature       | New functionality               |

| type: bug           | Broken or incorrect behavior    |

| type: documentation | README, docs, comments, runbook |

| type: refactor      | Code cleanup or restructuring   |

| type: test          | Test cases and validation       |

| type: dashboard     | Power BI or reporting work      |

| type: data-model    | SQL warehouse and schema work   |

| type: etl           | Python ETL pipeline work        |

| type: forecasting   | Forecast engine work            |

| type: optimization  | Inventory optimization work     |



\---



\### Priority Labels



| Label            | Purpose                  |

| ---------------- | ------------------------ |

| priority: high   | Important and urgent     |

| priority: medium | Important but not urgent |

| priority: low    | Nice to have             |



\---



\### Status Labels



| Label               | Purpose                   |

| ------------------- | ------------------------- |

| status: planned     | Planned but not started   |

| status: in-progress | Currently being worked on |

| status: blocked     | Waiting for dependency    |

| status: done        | Completed                 |



\---



\## Suggested Milestones



\### Milestone 1: Power BI Dashboard Foundation



Goal:



Build the first Power BI dashboard layer using mart views.



Suggested issues:



1\. Build executive KPI dashboard

2\. Build sales performance dashboard

3\. Build inventory position dashboard

4\. Build stock movement dashboard

5\. Create dashboard documentation



\---



\### Milestone 2: Forecast Engine



Goal:



Create Python forecasting module and load forecasts into SQL Server.



Suggested issues:



1\. Create forecast module structure

2\. Build baseline forecasting model

3\. Add forecast backtesting

4\. Add forecast accuracy metrics

5\. Load forecast output to SQL Server

6\. Add forecast dashboard mart view



\---



\### Milestone 3: Inventory Optimization Engine



Goal:



Create logic for reorder point, safety stock, stock health, and order recommendations.



Suggested issues:



1\. Build safety stock calculation

2\. Build reorder point calculation

3\. Build recommended order quantity logic

4\. Add ABC/XYZ/FSN classification

5\. Create inventory health score

6\. Load optimization output to SQL Server



\---



\### Milestone 4: AI Supply Chain Assistant



Goal:



Create a business assistant layer for retail supply chain questions.



Suggested issues:



1\. Define assistant use cases

2\. Create query templates

3\. Connect assistant to mart views

4\. Add question-answer examples

5\. Document AI assistant limitations



\---



\### Milestone 5: Web App and Deployment



Goal:



Create a simple web interface and prepare cloud deployment.



Suggested issues:



1\. Create Flask app structure

2\. Add ETL status page

3\. Add batch history page

4\. Add data quality error page

5\. Add forecast results page

6\. Add deployment documentation



\---



\## Recommended Initial GitHub Issues



Create these issues first:



\### Issue 1: Build Power BI Executive Dashboard



Description:



Create the first Power BI dashboard using `mart.vw\_executive\_kpi\_base`.



Acceptance criteria:



\* Dashboard connects to SQL Server

\* Shows net sales

\* Shows stock value

\* Shows gross margin

\* Shows forecast accuracy

\* Shows inventory health indicators

\* Screenshot added to documentation



Labels:



\* type: dashboard

\* priority: high

\* status: planned



\---



\### Issue 2: Build Sales Performance Dashboard



Description:



Create sales analysis dashboard using `mart.vw\_sales\_performance`.



Acceptance criteria:



\* Sales by date

\* Sales by product

\* Sales by location

\* Sales by channel

\* Gross margin analysis

\* Top and bottom products



Labels:



\* type: dashboard

\* priority: high

\* status: planned



\---



\### Issue 3: Create Forecast Engine Module



Description:



Create a new Python module for demand forecasting.



Acceptance criteria:



\* Forecast folder created

\* Baseline model added

\* Backtesting added

\* Forecast metrics calculated

\* Forecast output ready for SQL load



Labels:



\* type: forecasting

\* priority: high

\* status: planned



\---



\### Issue 4: Create Inventory Optimization Engine



Description:



Create inventory optimization calculations.



Acceptance criteria:



\* Safety stock calculated

\* Reorder point calculated

\* Recommended order quantity calculated

\* Inventory health score calculated

\* Output aligned with `dw.fact\_stock\_optimization`



Labels:



\* type: optimization

\* priority: high

\* status: planned



\---



\### Issue 5: Add Dashboard Screenshots to README



Description:



Add future Power BI dashboard screenshots to README.



Acceptance criteria:



\* Screenshots folder created

\* Dashboard images added

\* README updated with dashboard section

\* Images render correctly on GitHub



Labels:



\* type: documentation

\* priority: medium

\* status: planned



\---



\## Issue Naming Convention



Use this format:



```text

\[Area] Short action-based title

```



Examples:



```text

\[Power BI] Build executive KPI dashboard

\[Forecasting] Create baseline demand forecast model

\[Optimization] Add reorder point calculation

\[Docs] Add dashboard screenshots to README

\[ETL] Refactor file validation rules

```



\---



\## Branch Naming Convention



Use this format:



```text

feature/short-description

fix/short-description

docs/short-description

refactor/short-description

```



Examples:



```text

feature/power-bi-executive-dashboard

feature/forecast-engine-baseline

feature/inventory-optimization-engine

docs/add-dashboard-screenshots

fix/post-load-validation-counts

```



\---



\## Commit Message Convention



Use clear action-based commits.



Examples:



```text

Add executive KPI dashboard documentation

Create baseline forecast engine module

Add reorder point calculation

Fix transfer validation business rule

Update README with dashboard screenshots

```



\---



\## Pull Request Convention



Each pull request should include:



\* Summary

\* Files changed

\* Testing performed

\* Screenshots if dashboard/UI related

\* Risks or notes

\* Next steps



