-- Inventory Fact
-- Semi-additive across time:
-- closing_stock
-- stock_value

SELECT
    stock_date,
    brand,
    store_code,
    item_no,
    season,
    SUM(closing_stock) AS closing_stock,
    SUM(stock_value) AS stock_value
FROM stg_inventory
GROUP BY
    stock_date,
    brand,
    store_code,
    item_no,
    season;
