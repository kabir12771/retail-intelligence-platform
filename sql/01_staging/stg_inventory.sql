-- Staging Inventory
-- Purpose: Clean and standardize raw inventory data

SELECT
    CAST(stock_date AS DATE) AS stock_date,
    brand,
    store_code,
    item_no,
    season,
    closing_stock,
    unit_cost,
    closing_stock * unit_cost AS stock_value
FROM raw_inventory;
