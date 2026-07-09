-- Staging Sales
-- Purpose: Clean and standardize raw sales data

SELECT
    CAST(date AS DATE) AS sales_date,
    brand,
    store_code,
    item_no,
    style,
    season,
    qty,
    unit_price,
    qty * unit_price AS sales_value
FROM raw_sales;
