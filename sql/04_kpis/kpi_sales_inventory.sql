-- Sales and Inventory KPIs
-- Purpose:
-- Analyze sales performance and inventory position by brand, store, item, and season.
--
-- Business Questions Answered:
-- 1. What is total sales quantity?
-- 2. What is total sales value?
-- 3. Which brand/store/item is selling more?
-- 4. How much stock is available?
-- 5. What is the stock value?

SELECT
    s.brand,
    s.store_code,
    s.item_no,
    s.season,

    SUM(s.sales_qty) AS total_sales_qty,
    SUM(s.sales_value) AS total_sales_value,

    SUM(i.closing_stock) AS closing_stock_qty,
    SUM(i.stock_value) AS closing_stock_value,

    CASE
        WHEN SUM(s.sales_qty) = 0 THEN NULL
        ELSE SUM(i.closing_stock) * 1.0 / SUM(s.sales_qty)
    END AS stock_to_sales_ratio

FROM fact_sales s

LEFT JOIN fact_inventory i
    ON s.brand = i.brand
    AND s.store_code = i.store_code
    AND s.item_no = i.item_no
    AND s.season = i.season

GROUP BY
    s.brand,
    s.store_code,
    s.item_no,
    s.season

ORDER BY
    total_sales_value DESC;
