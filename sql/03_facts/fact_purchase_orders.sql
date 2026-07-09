-- Purchase Order Fact
-- Additive:
-- ordered_qty
-- received_qty
-- open_qty
-- open_cost_value
-- Non-additive:
-- unit_cost

SELECT
    po_no,
    vendor,
    brand,
    item_no,
    SUM(ordered_qty) AS ordered_qty,
    SUM(received_qty) AS received_qty,
    SUM(open_qty) AS open_qty,
    SUM(open_cost_value) AS open_cost_value
FROM raw_purchase_orders
GROUP BY
    po_no,
    vendor,
    brand,
    item_no;
