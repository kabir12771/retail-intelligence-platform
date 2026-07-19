import json
from datetime import date, datetime

import pandas as pd
from sqlalchemy import text

from config.file_config import get_file_config
from load.sql_connection import get_sql_engine


def make_json_safe(value):
    """
    Convert pandas / datetime values into JSON-safe values.
    """

    if pd.isna(value):
        return None

    if isinstance(value, (datetime, date)):
        return value.isoformat()

    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            return str(value)

    return value


def row_to_json(row: pd.Series) -> str:
    """
    Convert one pandas row into JSON text.
    """

    clean_record = {
        column: make_json_safe(value)
        for column, value in row.items()
    }

    return json.dumps(
        clean_record,
        ensure_ascii=False,
        default=str,
    )


def reset_batch_audit(batch_id: int) -> None:
    """
    Remove existing audit rows for the same batch_id.
    This keeps reruns clean during development.
    """

    engine = get_sql_engine()

    with engine.begin() as connection:
        connection.execute(
            text("DELETE FROM audit.data_quality_error_log WHERE batch_id = :batch_id"),
            {"batch_id": batch_id},
        )

        connection.execute(
            text("DELETE FROM audit.etl_file_log WHERE batch_id = :batch_id"),
            {"batch_id": batch_id},
        )

        connection.execute(
            text("DELETE FROM audit.etl_batch_log WHERE batch_id = :batch_id"),
            {"batch_id": batch_id},
        )


def start_batch_log(
    batch_id: int,
    pipeline_name: str,
    total_file_types: int,
) -> None:
    """
    Insert a new ETL batch audit record.
    """

    reset_batch_audit(batch_id)

    engine = get_sql_engine()

    insert_sql = text("""
        INSERT INTO audit.etl_batch_log (
            batch_id,
            pipeline_name,
            batch_status,
            started_at,
            total_file_types,
            successful_file_types,
            failed_file_types,
            total_rows_read,
            total_rows_loaded,
            created_at
        )
        VALUES (
            :batch_id,
            :pipeline_name,
            'RUNNING',
            SYSDATETIME(),
            :total_file_types,
            0,
            0,
            0,
            0,
            SYSDATETIME()
        );
    """)

    with engine.begin() as connection:
        connection.execute(
            insert_sql,
            {
                "batch_id": batch_id,
                "pipeline_name": pipeline_name,
                "total_file_types": total_file_types,
            },
        )

    print(f"Started audit batch log for batch_id={batch_id}")


def complete_batch_log(
    batch_id: int,
    batch_status: str,
    successful_file_types: int,
    failed_file_types: int,
    total_rows_read: int,
    total_rows_loaded: int,
    error_message: str | None = None,
) -> None:
    """
    Update final ETL batch audit status.
    """

    engine = get_sql_engine()

    update_sql = text("""
        UPDATE audit.etl_batch_log
        SET
            batch_status = :batch_status,
            completed_at = SYSDATETIME(),
            successful_file_types = :successful_file_types,
            failed_file_types = :failed_file_types,
            total_rows_read = :total_rows_read,
            total_rows_loaded = :total_rows_loaded,
            error_message = :error_message,
            updated_at = SYSDATETIME()
        WHERE batch_id = :batch_id;
    """)

    with engine.begin() as connection:
        connection.execute(
            update_sql,
            {
                "batch_id": batch_id,
                "batch_status": batch_status,
                "successful_file_types": successful_file_types,
                "failed_file_types": failed_file_types,
                "total_rows_read": total_rows_read,
                "total_rows_loaded": total_rows_loaded,
                "error_message": error_message,
            },
        )

    print(f"Completed audit batch log with status={batch_status}")


def log_file_result(
    batch_id: int,
    result: dict,
) -> None:
    """
    Insert one file-level audit row.
    """

    file_type = result["file_type"]

    try:
        staging_table = get_file_config(file_type)["staging_table"]
    except Exception:
        staging_table = None

    engine = get_sql_engine()

    insert_sql = text("""
        INSERT INTO audit.etl_file_log (
            batch_id,
            file_type,
            staging_table,
            file_status,
            rows_read,
            rows_loaded,
            invalid_rows,
            started_at,
            completed_at,
            message,
            created_at
        )
        VALUES (
            :batch_id,
            :file_type,
            :staging_table,
            :file_status,
            :rows_read,
            :rows_loaded,
            :invalid_rows,
            :started_at,
            :completed_at,
            :message,
            SYSDATETIME()
        );
    """)

    with engine.begin() as connection:
        connection.execute(
            insert_sql,
            {
                "batch_id": batch_id,
                "file_type": file_type,
                "staging_table": staging_table,
                "file_status": result["status"],
                "rows_read": result["rows_read"],
                "rows_loaded": result["rows_loaded"],
                "invalid_rows": result["invalid_rows"],
                "started_at": result.get("started_at"),
                "completed_at": result.get("completed_at"),
                "message": result.get("message"),
            },
        )


def log_data_quality_errors(
    batch_id: int,
    file_type: str,
    df: pd.DataFrame,
) -> int:
    """
    Save invalid rows into audit.data_quality_error_log.
    """

    if df.empty:
        return 0

    if "is_valid" not in df.columns:
        return 0

    invalid_df = df[df["is_valid"] == False].copy()

    if invalid_df.empty:
        return 0

    rows_to_insert = []

    for _, row in invalid_df.iterrows():
        source_row_number = row.get("source_row_number")

        if pd.isna(source_row_number):
            source_row_number = None
        else:
            source_row_number = int(source_row_number)

        rows_to_insert.append(
            {
                "batch_id": batch_id,
                "file_type": file_type,
                "source_file_name": row.get("source_file_name"),
                "source_row_number": source_row_number,
                "error_message": row.get("validation_message"),
                "raw_record_json": row_to_json(row),
            }
        )

    insert_sql = text("""
        INSERT INTO audit.data_quality_error_log (
            batch_id,
            file_type,
            source_file_name,
            source_row_number,
            error_message,
            raw_record_json,
            created_at
        )
        VALUES (
            :batch_id,
            :file_type,
            :source_file_name,
            :source_row_number,
            :error_message,
            :raw_record_json,
            SYSDATETIME()
        );
    """)

    engine = get_sql_engine()

    with engine.begin() as connection:
        connection.execute(insert_sql, rows_to_insert)

    print(f"Logged {len(rows_to_insert)} data quality errors for {file_type}")

    return len(rows_to_insert)