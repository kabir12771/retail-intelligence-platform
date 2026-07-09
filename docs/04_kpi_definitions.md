# KPI Definitions

## Sales Quantity

```text
Sales Qty = SUM(qty)
```

## Sales Value

```text
Sales Value = SUM(sales_value)
```

## Closing Stock

```text
Closing Stock = SUM(closing_stock)
```

## Stock Value

```text
Stock Value = SUM(stock_value)
```

## Open Purchase Order Quantity

```text
Open PO Qty = SUM(open_qty)
```

## In-Transit Quantity

```text
In-Transit Qty = SUM(in_transit_qty)
```

## Forecast Error Quantity

```text
Forecast Error Qty = Actual Qty - Forecast Qty
```

## Absolute Error Quantity

```text
Absolute Error Qty = ABS(Actual Qty - Forecast Qty)
```

## WAPE

```text
WAPE = SUM(Absolute Error Qty) / SUM(Actual Qty)
```

## Bias Percentage

```text
Bias % = SUM(Forecast Qty - Actual Qty) / SUM(Actual Qty)
```

Interpretation:

- Positive bias means over-forecasting
- Negative bias means under-forecasting

## Important Analytics Rule

Do not simply average percentages like MAPE or Bias across stores/items. Always calculate using numerator and denominator logic.
