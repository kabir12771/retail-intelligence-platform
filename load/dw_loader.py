from sqlalchemy import text

from load.sql_connection import get_sql_engine


DW_LOAD_PROCEDURES = [
    # Dimensions first
    "dw.usp_load_dim_product",
    "dw.usp_load_dim_location",
    "dw.usp_load_dim_supplier",

    # Facts after dimensions
    "dw.usp_load_fact_sales",
    "dw.usp_load_fact_inventory_snapshot",
    "dw.usp_load_fact_inventory_movement",
    "dw.usp_load_fact_purchase_orders",
    "dw.usp_load_fact_goods_receipts",
    "dw.usp_load_fact_transfers",
    "dw.usp_load_fact_forecast",
    "dw.usp_load_fact_stock_optimization",
]


def execute_dw_load_procedure(procedure_name: str, batch_id: int) -> None:
    """
    Execute one SQL Server stored procedure using batch_id.
    """

    engine = get_sql_engine()

    sql = text(f"EXEC {procedure_name} @batch_id = :batch_id;")

    with engine.begin() as connection:
        connection.execute(sql, {"batch_id": batch_id})

    print(f"Executed procedure: {procedure_name} for batch_id={batch_id}")


def execute_all_dw_load_procedures(batch_id: int) -> None:
    """
    Execute all DW load procedures in dependency order.
    """

    print("=" * 80)
    print(f"Starting DW load procedures for batch_id={batch_id}")
    print("=" * 80)

    for procedure_name in DW_LOAD_PROCEDURES:
        execute_dw_load_procedure(
            procedure_name=procedure_name,
            batch_id=batch_id,
        )

    print("=" * 80)
    print("All DW load procedures executed successfully.")


def get_dw_batch_row_counts(batch_id: int) -> list[dict]:
    """
    Return row counts from DW fact tables for a batch_id.
    Dimension tables are not batch-specific, so we count facts by batch_id.
    """

    engine = get_sql_engine()

    query = text("""
        SELECT 'dw.fact_sales' AS table_name, COUNT(*) AS row_count
        FROM dw.fact_sales
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_inventory_snapshot', COUNT(*)
        FROM dw.fact_inventory_snapshot
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_inventory_movement', COUNT(*)
        FROM dw.fact_inventory_movement
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_purchase_orders', COUNT(*)
        FROM dw.fact_purchase_orders
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_goods_receipts', COUNT(*)
        FROM dw.fact_goods_receipts
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_transfers', COUNT(*)
        FROM dw.fact_transfers
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_forecast', COUNT(*)
        FROM dw.fact_forecast
        WHERE batch_id = :batch_id

        UNION ALL
        SELECT 'dw.fact_stock_optimization', COUNT(*)
        FROM dw.fact_stock_optimization
        WHERE batch_id = :batch_id;
    """)

    with engine.connect() as connection:
        rows = connection.execute(query, {"batch_id": batch_id}).fetchall()

    return [
        {
            "table_name": row.table_name,
            "row_count": row.row_count,
        }
        for row in rows
    ]


def print_dw_batch_row_counts(batch_id: int) -> None:
    """
    Print fact row counts after DW loading.
    """

    row_counts = get_dw_batch_row_counts(batch_id)

    print("=" * 80)
    print(f"DW fact row counts for batch_id={batch_id}")
    print("=" * 80)

    for row in row_counts:
        print(f"{row['table_name']}: {row['row_count']}")