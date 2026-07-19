from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


def get_bool_env(variable_name: str, default: bool = False) -> bool:
    """
    Read boolean values from .env.
    Accepts: true, 1, yes, y
    """

    value = os.getenv(variable_name)

    if value is None:
        return default

    return value.strip().lower() in {"true", "1", "yes", "y"}


PIPELINE_NAME = os.getenv(
    "PIPELINE_NAME",
    "Retail Intelligence Platform ETL",
)

PIPELINE_ENV = os.getenv(
    "PIPELINE_ENV",
    "dev",
).strip().lower()

CLEAR_STAGING_BATCH = get_bool_env(
    "CLEAR_STAGING_BATCH",
    True,
)

ENABLE_POST_LOAD_VALIDATION = get_bool_env(
    "ENABLE_POST_LOAD_VALIDATION",
    True,
)

VALIDATE_MART_VIEWS = get_bool_env(
    "VALIDATE_MART_VIEWS",
    True,
)

MOVE_FILES_AFTER_SUCCESS = get_bool_env(
    "MOVE_FILES_AFTER_SUCCESS",
    True,
)

MOVE_REJECTED_FILES_ON_FAILURE = get_bool_env(
    "MOVE_REJECTED_FILES_ON_FAILURE",
    True,
)


FACT_FILE_TYPE_TO_TABLE = {
    "sales": "dw.fact_sales",
    "inventory_snapshot": "dw.fact_inventory_snapshot",
    "inventory_movement": "dw.fact_inventory_movement",
    "purchase_orders": "dw.fact_purchase_orders",
    "goods_receipts": "dw.fact_goods_receipts",
    "transfers": "dw.fact_transfers",
    "forecast": "dw.fact_forecast",
    "stock_optimization": "dw.fact_stock_optimization",
}


def build_expected_fact_counts_from_results(results: list[dict]) -> dict[str, int]:
    """
    Build expected DW fact counts dynamically from rows loaded to staging.

    This removes hardcoded expected fact counts from main.py.
    """

    expected_fact_counts = {}

    for result in results:
        file_type = result["file_type"]

        if file_type not in FACT_FILE_TYPE_TO_TABLE:
            continue

        if result["status"] != "SUCCESS":
            continue

        fact_table = FACT_FILE_TYPE_TO_TABLE[file_type]
        expected_fact_counts[fact_table] = result["rows_loaded"]

    return expected_fact_counts


def get_runtime_config_summary() -> dict:
    """
    Return runtime configuration for logging/printing.
    """

    return {
        "PIPELINE_NAME": PIPELINE_NAME,
        "PIPELINE_ENV": PIPELINE_ENV,
        "CLEAR_STAGING_BATCH": CLEAR_STAGING_BATCH,
        "ENABLE_POST_LOAD_VALIDATION": ENABLE_POST_LOAD_VALIDATION,
        "VALIDATE_MART_VIEWS": VALIDATE_MART_VIEWS,
        "MOVE_FILES_AFTER_SUCCESS": MOVE_FILES_AFTER_SUCCESS,
        "MOVE_REJECTED_FILES_ON_FAILURE": MOVE_REJECTED_FILES_ON_FAILURE,
    }


def print_runtime_config() -> None:
    """
    Print current runtime configuration.
    """

    print("=" * 80)
    print("PIPELINE RUNTIME CONFIGURATION")
    print("=" * 80)

    for key, value in get_runtime_config_summary().items():
        print(f"{key}: {value}")

    print("=" * 80)