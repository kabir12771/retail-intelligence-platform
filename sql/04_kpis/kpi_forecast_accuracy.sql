-- Forecast Accuracy KPIs
-- Purpose:
-- Measure how accurate the demand forecast is compared to actual sales.
--
-- Business Questions Answered:
-- 1. What was the forecast quantity?
-- 2. What was the actual sales quantity?
-- 3. What is the forecast error?
-- 4. What is the absolute forecast error?
-- 5. What is WAPE?
-- 6. What is forecast bias?
-- 7. Which store/item has the highest forecast error?
--
-- Important Rule:
-- Do not average row-level MAPE, WAPE, or bias percentages.
-- Always calculate forecast accuracy from summed numerator and denominator.

SELECT
    week_start,
    brand,
    store_code,
    item_no,

    SUM(forecast_qty) AS total_forecast_qty,
    SUM(actual_qty) AS total_actual_qty,

    SUM(actual_qty - forecast_qty) AS forecast_error_qty,
    SUM(ABS(actual_qty - forecast_qty)) AS absolute_error_qty,

    CASE
        WHEN SUM(actual_qty) = 0 THEN NULL
        ELSE SUM(ABS(actual_qty - forecast_qty)) * 1.0 / SUM(actual_qty)
    END AS wape,

    CASE
        WHEN SUM(actual_qty) = 0 THEN NULL
        ELSE SUM(forecast_qty - actual_qty) * 1.0 / SUM(actual_qty)
    END AS bias_percentage,

    CASE
        WHEN SUM(forecast_qty) > SUM(actual_qty) THEN 'Over Forecast'
        WHEN SUM(forecast_qty) < SUM(actual_qty) THEN 'Under Forecast'
        ELSE 'Perfect Forecast'
    END AS forecast_bias_status

FROM fact_forecast

GROUP BY
    week_start,
    brand,
    store_code,
    item_no

ORDER BY
    absolute_error_qty DESC;
