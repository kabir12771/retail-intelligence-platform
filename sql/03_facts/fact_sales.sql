-- Sales Fact
-- Additive measures:
-- qty
-- sales_value

SELECT
    sales_date,
    brand,
    store_code,
    item_no,
    season,
    SUM(qty) AS sales_qty,
    SUM(sales_value) AS sales_value
FROM stg_sales
GROUP BY
    sales_date,
    brand,
    store_code,
    item_no,
    season;
