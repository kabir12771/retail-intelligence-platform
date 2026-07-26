USE RetailIntelligenceDW;
GO

/* ==========================================================
   Retail Intelligence Platform
   Build 44A: Expand Forecast and Stock Optimization Demo Data

   Fixed version:
   - Does NOT insert identity keys
   - Removes ORDER BY forecast_date validation issue
   ========================================================== */

SET NOCOUNT ON;

------------------------------------------------------------
-- 1. Remove old demo expansion rows if script is re-run
------------------------------------------------------------

DELETE FROM dw.fact_forecast
WHERE forecast_batch_id = 'DEMO-FCST-EXP-20260719';

DELETE FROM dw.fact_stock_optimization
WHERE source_system = 'DEMO_OPTIMIZATION_EXPANSION'
   OR batch_id = 44001;


------------------------------------------------------------
-- 2. Build working sets from existing keys
------------------------------------------------------------

IF OBJECT_ID('tempdb..#products') IS NOT NULL DROP TABLE #products;
IF OBJECT_ID('tempdb..#locations') IS NOT NULL DROP TABLE #locations;
IF OBJECT_ID('tempdb..#weeks') IS NOT NULL DROP TABLE #weeks;

SELECT DISTINCT TOP (10)
    product_key
INTO #products
FROM (
    SELECT product_key FROM dw.fact_forecast
    UNION
    SELECT product_key FROM dw.fact_stock_optimization
) p
WHERE product_key > 0
ORDER BY product_key;

SELECT DISTINCT TOP (5)
    location_key
INTO #locations
FROM (
    SELECT location_key FROM dw.fact_forecast
    UNION
    SELECT location_key FROM dw.fact_stock_optimization
) l
WHERE location_key > 0
ORDER BY location_key;

CREATE TABLE #weeks (
    week_no INT NOT NULL,
    forecast_period_date_key INT NOT NULL,
    forecast_run_date_key INT NOT NULL
);

INSERT INTO #weeks (week_no, forecast_period_date_key, forecast_run_date_key)
VALUES
(1,  20260707, 20260701),
(2,  20260714, 20260701),
(3,  20260721, 20260701),
(4,  20260728, 20260701),
(5,  20260804, 20260701),
(6,  20260811, 20260701),
(7,  20260818, 20260701),
(8,  20260825, 20260701),
(9,  20260901, 20260701),
(10, 20260908, 20260701),
(11, 20260915, 20260701),
(12, 20260922, 20260701),
(13, 20260929, 20260701),
(14, 20261006, 20260701),
(15, 20261013, 20260701),
(16, 20261020, 20260701),
(17, 20261027, 20260701),
(18, 20261103, 20260701),
(19, 20261110, 20260701),
(20, 20261117, 20260701),
(21, 20261124, 20260701),
(22, 20261201, 20260701),
(23, 20261208, 20260701),
(24, 20261215, 20260701),
(25, 20261222, 20260701),
(26, 20261229, 20260701);


------------------------------------------------------------
-- 3. Expand Forecast Data
------------------------------------------------------------

;WITH base AS (
    SELECT
        p.product_key,
        l.location_key,
        w.week_no,
        w.forecast_period_date_key,
        w.forecast_run_date_key,
        CAST(1 AS INT) AS channel_key,
        CAST(1 AS INT) AS promotion_key,
        CAST(1 + ((p.product_key + l.location_key + w.week_no) % 4) AS INT) AS forecast_model_key,
        CAST(
            8
            + (p.product_key * 2)
            + (l.location_key * 3)
            + CASE 
                WHEN w.week_no BETWEEN 8 AND 12 THEN 5
                WHEN w.week_no BETWEEN 20 AND 26 THEN 7
                ELSE 0
              END
            + ((p.product_key + l.location_key + w.week_no) % 6)
            AS DECIMAL(18, 2)
        ) AS forecast_qty,
        CAST(
            CASE 
                WHEN (p.product_key + l.location_key + w.week_no) % 7 = 0 THEN -5
                WHEN (p.product_key + l.location_key + w.week_no) % 5 = 0 THEN 4
                WHEN (p.product_key + l.location_key + w.week_no) % 3 = 0 THEN -2
                ELSE 2
            END
            AS DECIMAL(18, 2)
        ) AS demand_variation
    FROM #products p
    CROSS JOIN #locations l
    CROSS JOIN #weeks w
),
calc AS (
    SELECT
        product_key,
        location_key,
        forecast_period_date_key,
        forecast_run_date_key,
        channel_key,
        promotion_key,
        forecast_model_key,
        forecast_qty,
        CASE 
            WHEN forecast_qty + demand_variation < 0 THEN 0
            ELSE forecast_qty + demand_variation
        END AS actual_qty
    FROM base
),
final_calc AS (
    SELECT
        product_key,
        location_key,
        forecast_period_date_key,
        forecast_run_date_key,
        channel_key,
        promotion_key,
        forecast_model_key,
        'V2' AS forecast_version,
        'DEMO-FCST-EXP-20260719' AS forecast_batch_id,
        forecast_qty,
        actual_qty,
        actual_qty - forecast_qty AS forecast_error_qty,
        ABS(actual_qty - forecast_qty) AS absolute_error_qty,
        POWER(actual_qty - forecast_qty, 2) AS squared_error_qty,
        CASE 
            WHEN actual_qty = 0 THEN NULL
            ELSE ABS(actual_qty - forecast_qty) / actual_qty
        END AS mape_percentage,
        CASE 
            WHEN actual_qty = 0 THEN NULL
            ELSE (actual_qty - forecast_qty) / actual_qty
        END AS bias_percentage,
        CASE 
            WHEN actual_qty = 0 THEN NULL
            ELSE 1 - (ABS(actual_qty - forecast_qty) / actual_qty)
        END AS forecast_accuracy_percentage
    FROM calc
)
INSERT INTO dw.fact_forecast (
    product_key,
    location_key,
    forecast_period_date_key,
    forecast_run_date_key,
    channel_key,
    promotion_key,
    forecast_model_key,
    forecast_version,
    forecast_batch_id,
    forecast_qty,
    actual_qty,
    forecast_error_qty,
    absolute_error_qty,
    squared_error_qty,
    mape_percentage,
    bias_percentage,
    forecast_accuracy_percentage,
    source_system,
    batch_id,
    created_at
)
SELECT
    product_key,
    location_key,
    forecast_period_date_key,
    forecast_run_date_key,
    channel_key,
    promotion_key,
    forecast_model_key,
    forecast_version,
    forecast_batch_id,
    forecast_qty,
    actual_qty,
    forecast_error_qty,
    absolute_error_qty,
    squared_error_qty,
    mape_percentage,
    bias_percentage,
    forecast_accuracy_percentage,
    'DEMO_FORECAST_EXPANSION' AS source_system,
    44001 AS batch_id,
    SYSDATETIME() AS created_at
FROM final_calc;


------------------------------------------------------------
-- 4. Expand Stock Optimization Data
------------------------------------------------------------

;WITH base AS (
    SELECT
        p.product_key,
        l.location_key,
        20260704 AS optimization_run_date_key,
        CAST(1 + ((p.product_key + l.location_key) % 3) AS INT) AS optimization_model_key,
        CAST(0.5 + ((p.product_key + l.location_key) % 8) * 0.35 AS DECIMAL(18, 2)) AS avg_daily_sales,
        CAST(0.2 + ((p.product_key + l.location_key) % 5) * 0.20 AS DECIMAL(18, 2)) AS demand_std_dev,
        CAST(10 + ((p.product_key + l.location_key) % 5) * 4 AS DECIMAL(18, 2)) AS lead_time_days,
        CAST(0.95 AS DECIMAL(18, 2)) AS service_level
    FROM #products p
    CROSS JOIN #locations l
),
calc AS (
    SELECT
        product_key,
        location_key,
        optimization_run_date_key,
        optimization_model_key,
        avg_daily_sales,
        demand_std_dev,
        lead_time_days,
        service_level,
        CAST(CEILING(demand_std_dev * SQRT(lead_time_days) * 1.65) AS DECIMAL(18, 2)) AS safety_stock_qty,
        CAST(CEILING((avg_daily_sales * lead_time_days) + (demand_std_dev * SQRT(lead_time_days) * 1.65)) AS DECIMAL(18, 2)) AS reorder_point_qty,
        CAST(
            CASE
                WHEN (product_key + location_key) % 4 = 0 THEN 0
                ELSE CEILING((avg_daily_sales * lead_time_days) * 1.20)
            END
            AS DECIMAL(18, 2)
        ) AS recommended_order_qty,
        CAST(
            CASE
                WHEN avg_daily_sales = 0 THEN 0
                ELSE CEILING((10 + ((product_key + location_key) % 50)) / avg_daily_sales)
            END
            AS DECIMAL(18, 2)
        ) AS stock_cover_days
    FROM base
),
final_calc AS (
    SELECT
        product_key,
        location_key,
        optimization_run_date_key,
        optimization_model_key,
        avg_daily_sales,
        demand_std_dev,
        lead_time_days,
        service_level,
        safety_stock_qty,
        reorder_point_qty,
        recommended_order_qty,
        stock_cover_days,
        CASE 
            WHEN avg_daily_sales >= 2.5 THEN 'A'
            WHEN avg_daily_sales >= 1.5 THEN 'B'
            ELSE 'C'
        END AS abc_class,
        CASE
            WHEN demand_std_dev <= 0.40 THEN 'X'
            WHEN demand_std_dev <= 0.80 THEN 'Y'
            ELSE 'Z'
        END AS xyz_class,
        CASE
            WHEN avg_daily_sales >= 2.0 THEN 'F'
            WHEN avg_daily_sales >= 1.0 THEN 'S'
            ELSE 'N'
        END AS fsn_class,
        CAST(
            CASE
                WHEN recommended_order_qty > 0 AND stock_cover_days < 14 THEN 45
                WHEN recommended_order_qty > 0 AND stock_cover_days BETWEEN 14 AND 35 THEN 70
                WHEN recommended_order_qty = 0 AND stock_cover_days > 45 THEN 62
                ELSE 82
            END
            AS DECIMAL(18, 2)
        ) AS inventory_health_score,
        CASE
            WHEN recommended_order_qty > 0 AND stock_cover_days < 14 THEN 'Critical stockout risk - replenish now'
            WHEN recommended_order_qty > 0 AND stock_cover_days BETWEEN 14 AND 35 THEN 'Reorder recommended'
            WHEN recommended_order_qty = 0 AND stock_cover_days > 45 THEN 'Monitor overstock risk'
            ELSE 'Healthy stock position'
        END AS recommendation
    FROM calc
)
INSERT INTO dw.fact_stock_optimization (
    product_key,
    location_key,
    optimization_run_date_key,
    optimization_model_key,
    avg_daily_sales,
    demand_std_dev,
    lead_time_days,
    service_level,
    safety_stock_qty,
    reorder_point_qty,
    recommended_order_qty,
    stock_cover_days,
    abc_class,
    xyz_class,
    fsn_class,
    inventory_health_score,
    recommendation,
    source_system,
    batch_id,
    created_at
)
SELECT
    product_key,
    location_key,
    optimization_run_date_key,
    optimization_model_key,
    avg_daily_sales,
    demand_std_dev,
    lead_time_days,
    service_level,
    safety_stock_qty,
    reorder_point_qty,
    recommended_order_qty,
    stock_cover_days,
    abc_class,
    xyz_class,
    fsn_class,
    inventory_health_score,
    recommendation,
    'DEMO_OPTIMIZATION_EXPANSION' AS source_system,
    44001 AS batch_id,
    SYSDATETIME() AS created_at
FROM final_calc;


------------------------------------------------------------
-- 5. Validation
------------------------------------------------------------

SELECT 'dw.fact_forecast' AS table_name, COUNT(*) AS row_count
FROM dw.fact_forecast

UNION ALL

SELECT 'mart.vw_forecast_accuracy' AS table_name, COUNT(*) AS row_count
FROM mart.vw_forecast_accuracy

UNION ALL

SELECT 'dw.fact_stock_optimization' AS table_name, COUNT(*) AS row_count
FROM dw.fact_stock_optimization

UNION ALL

SELECT 'mart.vw_stock_optimization' AS table_name, COUNT(*) AS row_count
FROM mart.vw_stock_optimization;


SELECT TOP 20 *
FROM mart.vw_forecast_accuracy;


SELECT TOP 20 *
FROM mart.vw_stock_optimization
ORDER BY inventory_health_score ASC;
GO