from sqlalchemy import text

from load.sql_connection import get_sql_engine


FACT_TABLES = [
    "dw.fact_sales",
    "dw.fact_inventory_snapshot",
    "dw.fact_inventory_movement",
    "dw.fact_purchase_orders",
    "dw.fact_goods_receipts",
    "dw.fact_transfers",
    "dw.fact_forecast",
    "dw.fact_stock_optimization",
]


MART_VIEWS = [
    "mart.vw_sales_performance",
    "mart.vw_inventory_position",
    "mart.vw_latest_inventory_position",
    "mart.vw_inventory_movement_analysis",
    "mart.vw_purchase_order_analysis",
    "mart.vw_goods_receipt_analysis",
    "mart.vw_transfer_analysis",
    "mart.vw_forecast_accuracy",
    "mart.vw_stock_optimization",
    "mart.vw_executive_kpi_base",
]


def get_latest_batch_id() -> int:
    """
    Get latest ETL batch id from audit table.
    """

    engine = get_sql_engine()

    query = text("""
        SELECT TOP 1 batch_id
        FROM audit.etl_batch_log
        ORDER BY started_at DESC;
    """)

    with engine.connect() as connection:
        batch_id = connection.execute(query).scalar()

    if batch_id is None:
        raise ValueError("No batch_id found in audit.etl_batch_log.")

    return int(batch_id)


def get_batch_status(batch_id: int) -> str | None:
    """
    Get audit batch status.
    """

    engine = get_sql_engine()

    query = text("""
        SELECT batch_status
        FROM audit.etl_batch_log
        WHERE batch_id = :batch_id;
    """)

    with engine.connect() as connection:
        status = connection.execute(
            query,
            {"batch_id": batch_id},
        ).scalar()

    return status


def get_file_log_count(batch_id: int) -> int:
    """
    Count file-level audit logs for batch.
    """

    engine = get_sql_engine()

    query = text("""
        SELECT COUNT(*)
        FROM audit.etl_file_log
        WHERE batch_id = :batch_id;
    """)

    with engine.connect() as connection:
        count = connection.execute(
            query,
            {"batch_id": batch_id},
        ).scalar()

    return int(count)


def get_fact_row_count(table_name: str, batch_id: int) -> int:
    """
    Count rows from a DW fact table for a specific batch.
    """

    engine = get_sql_engine()

    query = text(f"""
        SELECT COUNT(*)
        FROM {table_name}
        WHERE batch_id = :batch_id;
    """)

    with engine.connect() as connection:
        count = connection.execute(
            query,
            {"batch_id": batch_id},
        ).scalar()

    return int(count)


def get_object_row_count(object_name: str) -> int:
    """
    Count rows from a table or view.
    """

    engine = get_sql_engine()

    query = text(f"""
        SELECT COUNT(*)
        FROM {object_name};
    """)

    with engine.connect() as connection:
        count = connection.execute(query).scalar()

    return int(count)


def run_post_load_validation(
    batch_id: int,
    expected_fact_counts: dict[str, int] | None = None,
    expected_batch_status: str = "SUCCESS",
    expected_file_log_count: int = 11,
    validate_mart_views: bool = True,
) -> list[dict]:
    """
    Run post-load validation checks.

    In standalone test mode, expected batch status is usually SUCCESS.
    Inside main.py, expected batch status is RUNNING because the batch is
    completed only after post-load validation passes.
    """

    results = []

    batch_status = get_batch_status(batch_id)

    results.append(
        {
            "check_name": "Audit batch status",
            "object_name": "audit.etl_batch_log",
            "expected": expected_batch_status,
            "actual": batch_status,
            "passed": batch_status == expected_batch_status,
        }
    )

    file_log_count = get_file_log_count(batch_id)

    results.append(
        {
            "check_name": "Audit file log count",
            "object_name": "audit.etl_file_log",
            "expected": expected_file_log_count,
            "actual": file_log_count,
            "passed": file_log_count == expected_file_log_count,
        }
    )

    for fact_table in FACT_TABLES:
        actual_count = get_fact_row_count(
            table_name=fact_table,
            batch_id=batch_id,
        )

        expected_count = None

        if expected_fact_counts:
            expected_count = expected_fact_counts.get(fact_table)

        if expected_count is not None:
            passed = actual_count == expected_count
            expected_display = expected_count
        else:
            passed = actual_count >= 0
            expected_display = ">= 0"

        results.append(
            {
                "check_name": "DW fact row count",
                "object_name": fact_table,
                "expected": expected_display,
                "actual": actual_count,
                "passed": passed,
            }
        )

    if validate_mart_views:
        for mart_view in MART_VIEWS:
            actual_count = get_object_row_count(mart_view)

            results.append(
                {
                    "check_name": "Mart view row count",
                    "object_name": mart_view,
                    "expected": "> 0",
                    "actual": actual_count,
                    "passed": actual_count > 0,
                }
            )

    return results


def print_validation_results(results: list[dict]) -> None:
    """
    Print validation results in readable format.
    """

    print("=" * 80)
    print("POST-LOAD VALIDATION RESULTS")
    print("=" * 80)

    failed_checks = 0

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"

        if not result["passed"]:
            failed_checks += 1

        print(
            f"{status:<6} "
            f"{result['check_name']:<25} "
            f"{result['object_name']:<45} "
            f"Expected: {str(result['expected']):<10} "
            f"Actual: {result['actual']}"
        )

    print("-" * 80)
    print(f"Total Checks: {len(results)}")
    print(f"Failed Checks: {failed_checks}")
    print("=" * 80)

    if failed_checks > 0:
        raise ValueError("Post-load validation failed.")