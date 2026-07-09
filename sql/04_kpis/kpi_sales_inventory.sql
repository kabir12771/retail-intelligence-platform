-- Sales and Inventory KPIs

SELECT
    s.brand,
    s.store_code,
    s.item_no,
    SUM(s.sales_qty) AS sales_qty,
    SUM(s.sales_value) AS sales_value,
    SUM(i.closing_stock) AS closing_stock,
    SUM(i.stock_value) AS stock_value
FROM fact_sales s
LEFT JOIN fact_inventory i
    ON s.brand = i.brand
    AND s.store_code = i.store_code
    AND s.item_no = i.item_no
GROUP BY
    s.brand,
    s.store_code,
    s.item_no;
