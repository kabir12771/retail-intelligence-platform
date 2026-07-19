from dataclasses import dataclass
import pandas as pd

from validate.schema_validation import (
    prepare_validation_columns,
    append_validation_message,
)


@dataclass
class DataQualityResult:
    file_type: str
    is_valid: bool
    total_rows: int
    invalid_rows: int
    dataframe: pd.DataFrame


DATE_COLUMNS = {
    "product_master": ["launch_date", "discontinue_date"],
    "location_master": ["opening_date", "closing_date"],
    "supplier_master": [],
    "sales": ["transaction_date"],
    "inventory_snapshot": ["snapshot_date"],
    "inventory_movement": ["movement_date"],
    "purchase_orders": ["order_date", "expected_delivery_date"],
    "goods_receipts": ["receipt_date", "expected_delivery_date"],
    "transfers": [
        "transfer_created_date",
        "shipped_date",
        "received_date",
        "expected_receipt_date",
    ],
    "forecast": ["forecast_period_date", "forecast_run_date"],
    "stock_optimization": ["optimization_run_date"],
}


NUMERIC_COLUMNS = {
    "product_master": ["unit_cost", "retail_price", "vat_rate", "is_active"],
    "location_master": [
        "latitude",
        "longitude",
        "area_sqm",
        "warehouse_capacity_units",
        "warehouse_capacity_cbm",
        "is_active",
    ],
    "supplier_master": [
        "standard_lead_time_days",
        "minimum_order_qty",
        "is_active",
    ],
    "sales": [
        "sales_line_number",
        "sales_qty",
        "gross_sales_amount",
        "discount_amount",
        "net_sales_amount",
        "vat_amount",
        "unit_cost",
        "cost_amount",
        "unit_retail_price",
        "gross_margin_amount",
    ],
    "inventory_snapshot": [
        "stock_on_hand_qty",
        "available_qty",
        "reserved_qty",
        "in_transit_qty",
        "on_order_qty",
        "unit_cost",
        "unit_retail_price",
        "inventory_cost_value",
        "inventory_retail_value",
        "stock_cover_days",
    ],
    "inventory_movement": [
        "movement_document_line_number",
        "source_document_line_number",
        "movement_qty",
        "unit_cost",
        "unit_retail_price",
        "movement_cost_value",
        "movement_retail_value",
    ],
    "purchase_orders": [
        "po_line_number",
        "ordered_qty",
        "cancelled_qty",
        "open_qty",
        "remaining_qty",
        "carton_qty",
        "unit_cost",
        "ordered_cost_value",
    ],
    "goods_receipts": [
        "grn_line_number",
        "po_line_number",
        "received_qty",
        "accepted_qty",
        "rejected_qty",
        "short_qty",
        "excess_qty",
        "defect_qty",
        "carton_qty",
        "unit_cost",
        "received_cost_value",
    ],
    "transfers": [
        "transfer_line_number",
        "requested_transfer_qty",
        "shipped_qty",
        "received_qty",
        "short_qty",
        "excess_qty",
        "in_transit_qty",
        "carton_qty",
        "unit_cost",
        "unit_retail_price",
        "transfer_cost_value",
        "transfer_retail_value",
    ],
    "forecast": [
        "forecast_qty",
        "actual_qty",
        "forecast_error_qty",
        "absolute_error_qty",
        "squared_error_qty",
        "mape_percentage",
        "bias_percentage",
        "forecast_accuracy_percentage",
    ],
    "stock_optimization": [
        "avg_daily_sales",
        "demand_std_dev",
        "lead_time_days",
        "service_level",
        "safety_stock_qty",
        "reorder_point_qty",
        "recommended_order_qty",
        "stock_cover_days",
        "inventory_health_score",
    ],
}


NON_NEGATIVE_COLUMNS = {
    "product_master": ["unit_cost", "retail_price", "vat_rate"],
    "location_master": [
        "area_sqm",
        "warehouse_capacity_units",
        "warehouse_capacity_cbm",
    ],
    "supplier_master": [
        "standard_lead_time_days",
        "minimum_order_qty",
    ],
    "sales": [
        "sales_qty",
        "gross_sales_amount",
        "discount_amount",
        "net_sales_amount",
        "vat_amount",
        "unit_cost",
        "cost_amount",
        "unit_retail_price",
    ],
    "inventory_snapshot": [
        "stock_on_hand_qty",
        "available_qty",
        "reserved_qty",
        "in_transit_qty",
        "on_order_qty",
        "unit_cost",
        "unit_retail_price",
        "inventory_cost_value",
        "inventory_retail_value",
        "stock_cover_days",
    ],
    "inventory_movement": [
        "unit_cost",
        "unit_retail_price",
    ],
    "purchase_orders": [
        "ordered_qty",
        "cancelled_qty",
        "open_qty",
        "remaining_qty",
        "carton_qty",
        "unit_cost",
        "ordered_cost_value",
    ],
    "goods_receipts": [
        "received_qty",
        "accepted_qty",
        "rejected_qty",
        "short_qty",
        "excess_qty",
        "defect_qty",
        "carton_qty",
        "unit_cost",
        "received_cost_value",
    ],
    "transfers": [
        "requested_transfer_qty",
        "shipped_qty",
        "received_qty",
        "short_qty",
        "excess_qty",
        "in_transit_qty",
        "carton_qty",
        "unit_cost",
        "unit_retail_price",
        "transfer_cost_value",
        "transfer_retail_value",
    ],
    "forecast": [
        "forecast_qty",
        "actual_qty",
        "absolute_error_qty",
        "squared_error_qty",
        "mape_percentage",
        "forecast_accuracy_percentage",
    ],
    "stock_optimization": [
        "avg_daily_sales",
        "demand_std_dev",
        "lead_time_days",
        "service_level",
        "safety_stock_qty",
        "reorder_point_qty",
        "recommended_order_qty",
        "stock_cover_days",
        "inventory_health_score",
    ],
}


DUPLICATE_KEY_COLUMNS = {
    "product_master": ["product_code"],
    "location_master": ["location_code"],
    "supplier_master": ["supplier_code"],
    "sales": ["sales_transaction_id", "sales_line_number"],
    "inventory_snapshot": ["snapshot_date", "product_code", "location_code"],
    "inventory_movement": [
        "movement_document_number",
        "movement_document_line_number",
    ],
    "purchase_orders": ["po_number", "po_line_number"],
    "goods_receipts": ["grn_number", "grn_line_number"],
    "transfers": ["transfer_order_number", "transfer_line_number"],
    "forecast": [
        "product_code",
        "location_code",
        "forecast_period_date",
        "forecast_run_date",
        "forecast_model_code",
        "forecast_version",
    ],
    "stock_optimization": [
        "product_code",
        "location_code",
        "optimization_run_date",
        "optimization_model_code",
    ],
}


ALLOWED_VALUES = {
    "sales": {
        "channel_code": {"RETAIL", "ECOM", "MARKETPLACE", "OUTLET", "WHOLESALE"},
    },
    "inventory_movement": {
        "movement_type_code": {
            "SALE",
            "RETURN",
            "TRANSFER_IN",
            "TRANSFER_OUT",
            "PURCHASE_RECEIPT",
            "ADJUSTMENT_POSITIVE",
            "ADJUSTMENT_NEGATIVE",
            "DAMAGE",
            "SHRINKAGE",
            "STOCK_COUNT_CORRECTION",
        },
    },
    "purchase_orders": {
        "po_status_code": {
            "OPEN",
            "PENDING",
            "APPROVED",
            "PARTIAL",
            "COMPLETED",
            "CLOSED",
            "CANCELLED",
            "REJECTED",
            "PARTIALLY_RECEIVED",
            "FULLY_RECEIVED",
        },
    },
    "goods_receipts": {
        "receipt_status_code": {
            "OPEN",
            "PENDING",
            "APPROVED",
            "PARTIAL",
            "COMPLETED",
            "CLOSED",
            "CANCELLED",
            "REJECTED",
            "PARTIALLY_RECEIVED",
            "FULLY_RECEIVED",
        },
    },
    "transfers": {
        "transfer_status_code": {
            "OPEN",
            "PENDING",
            "APPROVED",
            "PARTIAL",
            "COMPLETED",
            "CLOSED",
            "CANCELLED",
            "REJECTED",
            "IN_TRANSIT",
            "SHIPPED",
            "RECEIVED",
        },
    },
    "forecast": {
        "channel_code": {"RETAIL", "ECOM", "MARKETPLACE", "OUTLET", "WHOLESALE"},
        "forecast_model_code": {
            "NAIVE",
            "MOVING_AVG",
            "SARIMAX",
            "XGBOOST",
            "LIGHTGBM",
        },
    },
    "stock_optimization": {
        "optimization_model_code": {
            "BASIC_ROP",
            "ABC_XYZ",
            "STOCK_HEALTH",
        },
        "abc_class": {"A", "B", "C"},
        "xyz_class": {"X", "Y", "Z"},
        "fsn_class": {"F", "S", "N"},
    },
}


def mark_invalid_rows(df: pd.DataFrame, mask: pd.Series, message: str) -> pd.DataFrame:
    """
    Mark rows as invalid and append validation message.
    """

    if not mask.any():
        return df

    df.loc[mask, "is_valid"] = False

    df.loc[mask, "validation_message"] = df.loc[
        mask, "validation_message"
    ].apply(
        lambda existing_message: append_validation_message(
            existing_message,
            message,
        )
    )

    return df


def is_not_blank(series: pd.Series) -> pd.Series:
    """
    Return True where values are not null and not blank strings.
    """

    return ~series.isna() & (series.astype(str).str.strip() != "")


def validate_date_columns(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate date columns and normalize valid dates.
    Safe for columns that are fully blank.
    """

    df = df.copy()

    for column in DATE_COLUMNS.get(file_type, []):
        if column not in df.columns:
            continue

        # Force object dtype so pandas allows strings/blank values safely
        df[column] = df[column].astype("object")

        non_blank_mask = is_not_blank(df[column])
        parsed_dates = pd.to_datetime(df[column], errors="coerce")

        invalid_mask = non_blank_mask & parsed_dates.isna()

        df = mark_invalid_rows(
            df,
            invalid_mask,
            f"Invalid date value in column: {column}",
        )

        valid_mask = non_blank_mask & ~parsed_dates.isna()

        # Only assign when valid values exist
        if valid_mask.any():
            df.loc[valid_mask, column] = parsed_dates.loc[valid_mask].dt.strftime("%Y-%m-%d")

        # Keep blank values as None for SQL loading
        blank_mask = ~non_blank_mask
        if blank_mask.any():
            df.loc[blank_mask, column] = None

    return df
    """
    Validate date columns and normalize valid dates.
    """

    df = df.copy()

    for column in DATE_COLUMNS.get(file_type, []):
        if column not in df.columns:
            continue

        non_blank_mask = is_not_blank(df[column])
        parsed_dates = pd.to_datetime(df[column], errors="coerce")

        invalid_mask = non_blank_mask & parsed_dates.isna()

        df = mark_invalid_rows(
            df,
            invalid_mask,
            f"Invalid date value in column: {column}",
        )

        valid_mask = non_blank_mask & ~parsed_dates.isna()
        df.loc[valid_mask, column] = parsed_dates.loc[valid_mask].dt.strftime("%Y-%m-%d")

    return df


def validate_numeric_columns(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate numeric columns and normalize valid numeric values.
    """

    df = df.copy()

    for column in NUMERIC_COLUMNS.get(file_type, []):
        if column not in df.columns:
            continue

        non_blank_mask = is_not_blank(df[column])
        parsed_numbers = pd.to_numeric(df[column], errors="coerce")

        invalid_mask = non_blank_mask & parsed_numbers.isna()

        df = mark_invalid_rows(
            df,
            invalid_mask,
            f"Invalid numeric value in column: {column}",
        )

        valid_mask = non_blank_mask & ~parsed_numbers.isna()
        df.loc[valid_mask, column] = parsed_numbers.loc[valid_mask]

    return df


def validate_non_negative_columns(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate columns that must not be negative.
    """

    df = df.copy()

    for column in NON_NEGATIVE_COLUMNS.get(file_type, []):
        if column not in df.columns:
            continue

        numeric_values = pd.to_numeric(df[column], errors="coerce")
        invalid_mask = is_not_blank(df[column]) & (numeric_values < 0)

        df = mark_invalid_rows(
            df,
            invalid_mask,
            f"Negative value not allowed in column: {column}",
        )

    return df


def validate_duplicate_business_keys(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate duplicate business keys based on expected grain.
    """

    df = df.copy()

    key_columns = DUPLICATE_KEY_COLUMNS.get(file_type, [])

    if not key_columns:
        return df

    missing_key_columns = [
        column for column in key_columns
        if column not in df.columns
    ]

    if missing_key_columns:
        return df

    duplicate_mask = df.duplicated(subset=key_columns, keep=False)

    df = mark_invalid_rows(
        df,
        duplicate_mask,
        "Duplicate business key found: " + ", ".join(key_columns),
    )

    return df


def validate_allowed_values(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate selected code/status columns against allowed values.
    """

    df = df.copy()

    rules = ALLOWED_VALUES.get(file_type, {})

    for column, allowed_set in rules.items():
        if column not in df.columns:
            continue

        non_blank_mask = is_not_blank(df[column])

        normalized_values = (
            df[column]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        invalid_mask = non_blank_mask & ~normalized_values.isin(allowed_set)

        df = mark_invalid_rows(
            df,
            invalid_mask,
            f"Invalid value in column: {column}. Allowed values: {sorted(allowed_set)}",
        )

        df.loc[non_blank_mask, column] = normalized_values.loc[non_blank_mask]

    return df


def validate_business_rules(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate file-specific business rules.
    """

    df = df.copy()

    if file_type == "sales":
        if {"gross_sales_amount", "discount_amount", "net_sales_amount"}.issubset(df.columns):
            gross = pd.to_numeric(df["gross_sales_amount"], errors="coerce")
            discount = pd.to_numeric(df["discount_amount"], errors="coerce")
            net = pd.to_numeric(df["net_sales_amount"], errors="coerce")

            invalid_mask = (
                is_not_blank(df["gross_sales_amount"])
                & is_not_blank(df["discount_amount"])
                & is_not_blank(df["net_sales_amount"])
                & ((gross - discount - net).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                invalid_mask,
                "Sales amount mismatch: gross_sales_amount - discount_amount must equal net_sales_amount",
            )

    if file_type == "inventory_snapshot":
        if {"stock_on_hand_qty", "unit_cost", "inventory_cost_value"}.issubset(df.columns):
            stock = pd.to_numeric(df["stock_on_hand_qty"], errors="coerce")
            unit_cost = pd.to_numeric(df["unit_cost"], errors="coerce")
            cost_value = pd.to_numeric(df["inventory_cost_value"], errors="coerce")

            invalid_mask = (
                is_not_blank(df["stock_on_hand_qty"])
                & is_not_blank(df["unit_cost"])
                & is_not_blank(df["inventory_cost_value"])
                & ((stock * unit_cost - cost_value).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                invalid_mask,
                "Inventory cost mismatch: stock_on_hand_qty * unit_cost must equal inventory_cost_value",
            )

    if file_type == "transfers":
        if {
            "shipped_qty",
            "received_qty",
            "short_qty",
            "excess_qty",
            "transfer_status_code",
        }.issubset(df.columns):

            shipped = pd.to_numeric(df["shipped_qty"], errors="coerce")
            received = pd.to_numeric(df["received_qty"], errors="coerce")
            short = pd.to_numeric(df["short_qty"], errors="coerce")
            excess = pd.to_numeric(df["excess_qty"], errors="coerce")

            status = (
                df["transfer_status_code"]
                .astype(str)
                .str.strip()
                .str.upper()
            )

            completed_status_mask = status.isin(
                {"RECEIVED", "COMPLETED", "CLOSED"}
            )

            short_invalid_mask = (
                completed_status_mask
                & is_not_blank(df["shipped_qty"])
                & is_not_blank(df["received_qty"])
                & is_not_blank(df["short_qty"])
                & (shipped > received)
                & ((shipped - received - short).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                short_invalid_mask,
                "Transfer short quantity mismatch: shipped_qty - received_qty must equal short_qty only for completed transfers",
            )

            excess_invalid_mask = (
                completed_status_mask
                & is_not_blank(df["shipped_qty"])
                & is_not_blank(df["received_qty"])
                & is_not_blank(df["excess_qty"])
                & (received > shipped)
                & ((received - shipped - excess).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                excess_invalid_mask,
                "Transfer excess quantity mismatch: received_qty - shipped_qty must equal excess_qty only for completed transfers",
            )

    return df
    """
    Validate file-specific business rules.
    """

    df = df.copy()

    if file_type == "sales":
        if {"gross_sales_amount", "discount_amount", "net_sales_amount"}.issubset(df.columns):
            gross = pd.to_numeric(df["gross_sales_amount"], errors="coerce")
            discount = pd.to_numeric(df["discount_amount"], errors="coerce")
            net = pd.to_numeric(df["net_sales_amount"], errors="coerce")

            invalid_mask = (
                is_not_blank(df["gross_sales_amount"])
                & is_not_blank(df["discount_amount"])
                & is_not_blank(df["net_sales_amount"])
                & ((gross - discount - net).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                invalid_mask,
                "Sales amount mismatch: gross_sales_amount - discount_amount must equal net_sales_amount",
            )

    if file_type == "inventory_snapshot":
        if {"stock_on_hand_qty", "unit_cost", "inventory_cost_value"}.issubset(df.columns):
            stock = pd.to_numeric(df["stock_on_hand_qty"], errors="coerce")
            unit_cost = pd.to_numeric(df["unit_cost"], errors="coerce")
            cost_value = pd.to_numeric(df["inventory_cost_value"], errors="coerce")

            invalid_mask = (
                is_not_blank(df["stock_on_hand_qty"])
                & is_not_blank(df["unit_cost"])
                & is_not_blank(df["inventory_cost_value"])
                & ((stock * unit_cost - cost_value).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                invalid_mask,
                "Inventory cost mismatch: stock_on_hand_qty * unit_cost must equal inventory_cost_value",
            )

    if file_type == "transfers":
        if {"shipped_qty", "received_qty", "short_qty"}.issubset(df.columns):
            shipped = pd.to_numeric(df["shipped_qty"], errors="coerce")
            received = pd.to_numeric(df["received_qty"], errors="coerce")
            short = pd.to_numeric(df["short_qty"], errors="coerce")

            invalid_mask = (
                is_not_blank(df["shipped_qty"])
                & is_not_blank(df["received_qty"])
                & is_not_blank(df["short_qty"])
                & (shipped > received)
                & ((shipped - received - short).abs() > 0.05)
            )

            df = mark_invalid_rows(
                df,
                invalid_mask,
                "Transfer short quantity mismatch: shipped_qty - received_qty must equal short_qty when shipped is greater",
            )

    return df


def run_data_quality_checks(df: pd.DataFrame, file_type: str) -> DataQualityResult:
    """
    Run all data quality checks for one file type.
    """

    if df.empty:
        return DataQualityResult(
            file_type=file_type,
            is_valid=False,
            total_rows=0,
            invalid_rows=0,
            dataframe=df,
        )

    validated_df = prepare_validation_columns(df)

    validated_df = validate_date_columns(validated_df, file_type)
    validated_df = validate_numeric_columns(validated_df, file_type)
    validated_df = validate_non_negative_columns(validated_df, file_type)
    validated_df = validate_duplicate_business_keys(validated_df, file_type)
    validated_df = validate_allowed_values(validated_df, file_type)
    validated_df = validate_business_rules(validated_df, file_type)

    invalid_rows = int((validated_df["is_valid"] == False).sum())
    is_valid = invalid_rows == 0

    return DataQualityResult(
        file_type=file_type,
        is_valid=is_valid,
        total_rows=len(validated_df),
        invalid_rows=invalid_rows,
        dataframe=validated_df,
    )