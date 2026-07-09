-- Purchase Order Fact
-- Purpose:
-- Track purchase order quantities and remaining open cost value.
--
-- Business Questions Answered:
-- 1. What is total ordered quantity?
-- 2. What is total received quantity?
-- 3. What is open purchase order quantity?
-- 4. What is remaining purchase order cost value?
-- 5. Which vendor has the highest open quantity?
-- 6. Which brand/item has pending purchase quantity?
--
-- Measure Behavior:
-- Additive:
-- ordered_qty
-- received_qty
-- open_qty
-- open_cost_value
--
-- Non-additive:
-- unit_cost should not be summed.

SELECT
    po_no,
    vendor,
    brand,
    item_no,

    SUM(ordered_qty) AS total_ordered_qty,
    SUM(received_qty) AS total_received_qty,
    SUM(open_qty) AS open_po_qty,
    SUM(open_cost_value) AS open_po_cost_value,

    CASE
        WHEN SUM(ordered_qty) = 0 THEN NULL
        ELSE SUM(received_qty) * 1.0 / SUM(ordered_qty)
    END AS receipt_completion_rate,

    CASE
        WHEN SUM(open_qty) > 0 THEN 'Open'
        ELSE 'Closed'
    END AS po_status

FROM raw_purchase_orders

GROUP BY
    po_no,
    vendor,
    brand,
    item_no

ORDER BY
    open_po_qty DESC;
