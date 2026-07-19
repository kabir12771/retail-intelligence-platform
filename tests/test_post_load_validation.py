from validate.post_load_validation import (
    get_latest_batch_id,
    run_post_load_validation,
    print_validation_results,
)


EXPECTED_FACT_COUNTS = {
    "dw.fact_sales": 6,
    "dw.fact_inventory_snapshot": 6,
    "dw.fact_inventory_movement": 5,
    "dw.fact_purchase_orders": 3,
    "dw.fact_goods_receipts": 2,
    "dw.fact_transfers": 2,
    "dw.fact_forecast": 3,
    "dw.fact_stock_optimization": 3,
}


if __name__ == "__main__":
    batch_id = get_latest_batch_id()

    print(f"Validating latest batch_id: {batch_id}")

    results = run_post_load_validation(
        batch_id=batch_id,
        expected_fact_counts=EXPECTED_FACT_COUNTS,
    )

    print_validation_results(results)