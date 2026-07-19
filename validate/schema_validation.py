from dataclasses import dataclass
import pandas as pd

from config.file_config import get_file_config


@dataclass
class SchemaValidationResult:
    file_type: str
    is_valid: bool
    missing_columns: list[str]
    total_rows: int
    invalid_rows: int
    dataframe: pd.DataFrame


def append_validation_message(existing_message, new_message: str) -> str:
    """
    Append validation messages safely.
    """

    if pd.isna(existing_message) or existing_message in [None, ""]:
        return new_message

    return f"{existing_message} | {new_message}"


def validate_required_columns(df: pd.DataFrame, file_type: str) -> list[str]:
    """
    Check whether all required columns exist in the DataFrame.
    """

    config = get_file_config(file_type)
    required_columns = config["required_columns"]

    existing_columns = list(df.columns)

    missing_columns = [
        column for column in required_columns
        if column not in existing_columns
    ]

    return missing_columns


def prepare_validation_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure is_valid and validation_message columns exist.
    """

    df = df.copy()

    if "is_valid" not in df.columns:
        df["is_valid"] = True

    if "validation_message" not in df.columns:
        df["validation_message"] = None

    return df


def validate_required_values(df: pd.DataFrame, file_type: str) -> pd.DataFrame:
    """
    Validate that required columns do not contain blank/null values.
    """

    df = prepare_validation_columns(df)

    config = get_file_config(file_type)
    required_columns = config["required_columns"]

    for column in required_columns:
        if column not in df.columns:
            continue

        blank_mask = df[column].isna() | (df[column].astype(str).str.strip() == "")

        if blank_mask.any():
            df.loc[blank_mask, "is_valid"] = False
            df.loc[blank_mask, "validation_message"] = df.loc[
                blank_mask, "validation_message"
            ].apply(
                lambda message: append_validation_message(
                    message,
                    f"Missing required value in column: {column}"
                )
            )

    return df


def validate_schema(df: pd.DataFrame, file_type: str) -> SchemaValidationResult:
    """
    Full schema validation:
    1. Check required columns exist.
    2. Check required values are not blank.
    3. Return validation result and validated DataFrame.
    """

    if df.empty:
        return SchemaValidationResult(
            file_type=file_type,
            is_valid=False,
            missing_columns=[],
            total_rows=0,
            invalid_rows=0,
            dataframe=df,
        )

    missing_columns = validate_required_columns(df, file_type)

    if missing_columns:
        validated_df = prepare_validation_columns(df)
        validated_df["is_valid"] = False
        validated_df["validation_message"] = (
            "Missing required columns: " + ", ".join(missing_columns)
        )

        return SchemaValidationResult(
            file_type=file_type,
            is_valid=False,
            missing_columns=missing_columns,
            total_rows=len(validated_df),
            invalid_rows=len(validated_df),
            dataframe=validated_df,
        )

    validated_df = validate_required_values(df, file_type)

    invalid_rows = int((validated_df["is_valid"] == False).sum())
    is_valid = invalid_rows == 0

    return SchemaValidationResult(
        file_type=file_type,
        is_valid=is_valid,
        missing_columns=[],
        total_rows=len(validated_df),
        invalid_rows=invalid_rows,
        dataframe=validated_df,
    )