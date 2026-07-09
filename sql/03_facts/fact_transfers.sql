-- Transfer Fact
-- Additive:
-- requested_transfer_qty
-- shipped_qty
-- received_qty
-- short_qty
-- excess_qty
-- in_transit_qty

SELECT
    transfer_no,
    transfer_from,
    transfer_to,
    item_no,
    SUM(requested_transfer_qty) AS requested_transfer_qty,
    SUM(shipped_qty) AS shipped_qty,
    SUM(received_qty) AS received_qty,
    SUM(short_qty) AS short_qty,
    SUM(excess_qty) AS excess_qty,
    SUM(in_transit_qty) AS in_transit_qty
FROM raw_transfers
GROUP BY
    transfer_no,
    transfer_from,
    transfer_to,
    item_no;
