from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "input_files"
PROCESSED_DIR = BASE_DIR / "processed_files"
REJECTED_DIR = BASE_DIR / "rejected_files"
ERROR_REPORT_DIR = BASE_DIR / "error_reports"
LOG_DIR = BASE_DIR / "logs"


FILE_CONFIG = {
    "product_master": {
        "input_folder": INPUT_DIR / "product_master",
        "staging_table": "stg.product",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "product_code",
            "product_name",
            "brand",
            "category",
            "unit_cost",
            "retail_price",
        ],
    },

    "location_master": {
        "input_folder": INPUT_DIR / "location_master",
        "staging_table": "stg.location",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "location_code",
            "location_name",
            "location_type",
            "country",
            "city",
        ],
    },

    "supplier_master": {
        "input_folder": INPUT_DIR / "supplier_master",
        "staging_table": "stg.supplier",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "supplier_code",
            "supplier_name",
            "supplier_country",
            "standard_lead_time_days",
        ],
    },

    "sales": {
        "input_folder": INPUT_DIR / "sales",
        "staging_table": "stg.sales",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "sales_transaction_id",
            "sales_receipt_number",
            "sales_line_number",
            "product_code",
            "location_code",
            "transaction_date",
            "sales_qty",
            "net_sales_amount",
        ],
    },

    "inventory_snapshot": {
        "input_folder": INPUT_DIR / "inventory_snapshot",
        "staging_table": "stg.inventory_snapshot",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "snapshot_date",
            "product_code",
            "location_code",
            "stock_on_hand_qty",
        ],
    },

    "inventory_movement": {
        "input_folder": INPUT_DIR / "inventory_movement",
        "staging_table": "stg.inventory_movement",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "movement_document_number",
            "movement_document_line_number",
            "product_code",
            "location_code",
            "movement_date",
            "movement_type_code",
            "movement_qty",
        ],
    },

    "purchase_orders": {
        "input_folder": INPUT_DIR / "purchase_orders",
        "staging_table": "stg.purchase_orders",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "po_number",
            "po_line_number",
            "product_code",
            "supplier_code",
            "receiving_location_code",
            "order_date",
            "ordered_qty",
        ],
    },

    "goods_receipts": {
        "input_folder": INPUT_DIR / "goods_receipts",
        "staging_table": "stg.goods_receipts",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "grn_number",
            "grn_line_number",
            "product_code",
            "supplier_code",
            "receiving_location_code",
            "receipt_date",
            "received_qty",
        ],
    },

    "transfers": {
        "input_folder": INPUT_DIR / "transfers",
        "staging_table": "stg.transfers",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "transfer_order_number",
            "transfer_line_number",
            "product_code",
            "from_location_code",
            "to_location_code",
            "transfer_created_date",
        ],
    },

    "forecast": {
        "input_folder": INPUT_DIR / "forecast",
        "staging_table": "stg.forecast",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "product_code",
            "location_code",
            "forecast_period_date",
            "forecast_run_date",
            "forecast_qty",
        ],
    },

    "stock_optimization": {
        "input_folder": INPUT_DIR / "stock_optimization",
        "staging_table": "stg.stock_optimization",
        "file_pattern": "*.xlsx",
        "required_columns": [
            "product_code",
            "location_code",
            "optimization_run_date",
        ],
    },
}


def get_file_config(file_type: str) -> dict:
    """
    Return configuration for one source file type.
    """

    if file_type not in FILE_CONFIG:
        raise ValueError(f"Unknown file type: {file_type}")

    return FILE_CONFIG[file_type]


def get_all_file_types() -> list:
    """
    Return all supported file types.
    """

    return list(FILE_CONFIG.keys())