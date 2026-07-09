-- Product Dimension
-- Purpose: One row per product/item

SELECT DISTINCT
    item_no,
    style,
    season,
    brand
FROM stg_sales;
