-- Forecast Accuracy KPIs
-- Do not average MAPE from row level.

SELECT
    brand,
    store_code,
    item_no,
    SUM(forecast_qty) AS forecast_qty,
    SUM(actual_qty) AS actual_qty,
    SUM(absolute_error_qty) AS absolute_error_qty,
    CASE
        WHEN SUM(actual_qty) = 0 THEN NULL
        ELSE SUM(absolute_error_qty) * 1.0 / SUM(actual_qty)
    END AS wape,
    CASE
        WHEN SUM(actual_qty) = 0 THEN NULL
        ELSE SUM(forecast_qty - actual_qty) * 1.0 / SUM(actual_qty)
    END AS bias_percentage
FROM fact_forecast
GROUP BY
    brand,
    store_code,
    item_no;
