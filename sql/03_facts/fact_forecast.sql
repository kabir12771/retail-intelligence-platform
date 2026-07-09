-- Forecast Fact
-- Important:
-- forecast_qty and actual_qty can be summed.
-- percentages should be calculated at report level, not averaged directly.

SELECT
    week_start,
    brand,
    store_code,
    item_no,
    SUM(forecast_qty) AS forecast_qty,
    SUM(actual_qty) AS actual_qty,
    SUM(actual_qty - forecast_qty) AS forecast_error_qty,
    SUM(ABS(actual_qty - forecast_qty)) AS absolute_error_qty
FROM raw_forecast
GROUP BY
    week_start,
    brand,
    store_code,
    item_no;
