# Retail Intelligence Platform

A beginner-friendly, portfolio-ready retail analytics project focused on **sales, inventory, purchase orders, transfers, and forecast accuracy**.

This project is designed for learning GitHub, SQL, Python, Power BI, and business analytics in a clean professional structure.

> Important: Use only sample or fake data. Do not upload private company data.

---

## Business Objective

Retail teams need to understand:

- What is selling?
- Where stock is available?
- Which stores are short or overstocked?
- Which purchase orders are still open?
- Which transfers are pending?
- How accurate the forecast is?

This project converts raw retail data into clean analytical tables and dashboards.

---

## Project Modules

| Module | Purpose |
|---|---|
| Sales Analysis | Analyze sales by store, item, brand, season, and date |
| Inventory Analysis | Track closing stock, stock value, and stock cover |
| Purchase Orders | Monitor ordered quantity, received quantity, open quantity, and cost |
| Transfers | Track requested, shipped, received, short, excess, and in-transit quantity |
| Forecast Accuracy | Compare forecast vs actual sales and calculate WAPE, MAPE, bias |
| Power BI Dashboard | Present KPIs and business insights visually |

---

## Tools Used

- SQL
- Python
- Power BI
- Excel / Power Query
- GitHub

---

## Folder Structure

```text
retail-intelligence-platform/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── data/
│   ├── raw_sample/
│   └── processed_sample/
├── docs/
├── notebooks/
├── powerbi/
│   └── dashboard_screenshots/
├── python/
│   ├── src/
│   └── tests/
├── sql/
│   ├── 01_staging/
│   ├── 02_dimensions/
│   ├── 03_facts/
│   └── 04_kpis/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Learning Path

Start in this order:

1. Read `docs/01_github_basics.md`
2. Read `docs/02_business_context.md`
3. Open sample CSV files in `data/raw_sample/`
4. Study SQL files in `sql/`
5. Run Python cleaning script in `python/src/`
6. Add screenshots later in `powerbi/dashboard_screenshots/`
7. Update this README as your project improves

---

## Key KPIs

| KPI | Meaning |
|---|---|
| Sales Qty | Total units sold |
| Sales Value | Quantity × selling price |
| Closing Stock | Stock available at period end |
| Stock Value | Closing stock × unit cost |
| Open PO Qty | Ordered quantity still not received |
| In-Transit Qty | Shipped but not yet received |
| WAPE | Forecast error compared to total actual sales |
| Bias % | Whether forecast is over or under actual sales |

---

## Project Status

Learning version created. More business logic and dashboards will be added step by step.
