# Data Dictionary

## sales_sample.csv

| Column | Description |
|---|---|
| date | Sales transaction date |
| brand | Brand name |
| store_code | Store code |
| item_no | Item number |
| style | Style code |
| season | Season code |
| qty | Sales quantity |
| unit_price | Selling price per unit |
| sales_value | qty × unit_price |

## inventory_sample.csv

| Column | Description |
|---|---|
| stock_date | Inventory date |
| brand | Brand name |
| store_code | Store code |
| item_no | Item number |
| season | Season code |
| closing_stock | Stock quantity |
| unit_cost | Cost per unit |
| stock_value | closing_stock × unit_cost |

## purchase_orders_sample.csv

| Column | Description |
|---|---|
| po_no | Purchase order number |
| vendor | Vendor name |
| brand | Brand name |
| item_no | Item number |
| ordered_qty | Quantity ordered |
| received_qty | Quantity received |
| open_qty | ordered_qty - received_qty |
| unit_cost | Cost per unit |
| open_cost_value | open_qty × unit_cost |

## transfers_sample.csv

| Column | Description |
|---|---|
| transfer_no | Transfer order number |
| transfer_from | Source location |
| transfer_to | Destination location |
| item_no | Item number |
| requested_transfer_qty | Requested transfer quantity |
| shipped_qty | Shipped quantity |
| received_qty | Received quantity |
| short_qty | shipped_qty - received_qty if positive |
| excess_qty | received_qty - shipped_qty if positive |
| in_transit_qty | shipped_qty - received_qty |

## forecast_sample.csv

| Column | Description |
|---|---|
| week_start | Forecast week |
| brand | Brand name |
| store_code | Store code |
| item_no | Item number |
| forecast_qty | Forecasted sales quantity |
| actual_qty | Actual sales quantity |
| forecast_error_qty | actual_qty - forecast_qty |
| absolute_error_qty | absolute value of forecast_error_qty |
