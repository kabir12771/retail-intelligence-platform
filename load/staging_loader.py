import pandas as pd
from sqlalchemy import text

from config.file_config import get_file_config
from config.column_mapping import get_column_mapping
from load.sql_connection import get_sql_engine


def split_schema_table(full_table_name: str) -> tuple[str, str]:
    """
    Split table name like 'stg.product' into schema and table.
    """

    if "." not in full_table_name:
        raise ValueError(
            f"Invalid table name: {full_table_name}. Expected format: schema.table"
        )

    schema_name, table_name = full_table_name.split(".", 1)

    return schema_name, table_name


def get_target_columns(engine, staging_table: str) -> list[str]:
    """
    Get target SQL table columns, excluding:
    - identity columns
    - computed columns
    - created_at because SQL Server default should populate it
    """

    schema_name, table_name = split_schema_table(staging_table)

    query = text("""
        SELECT
            c.name AS column_name
        FROM sys.columns c
        INNER JOIN sys.objects o
            ON c.object_id = o.object_id
        INNER JOIN sys.schemas s
            ON o.schema_id = s.schema_id
        WHERE s.name = :schema_name
          AND o.name = :table_name
          AND o.type = 'U'
          AND c.is_identity = 0
          AND c.is_computed = 0
          AND c.name <> 'created_at'
        ORDER BY c.column_id;
    """)

    with engine.connect() as connection:
        rows = connection.execute(
            query,
            {
                "schema_name": schema_name,
                "table_name": table_name,
            },
        ).fetchall()

    columns = [row.column_name for row in rows]

    if not columns:
        raise ValueError(f"No target columns found for table: {staging_table}")

    return columns


def clear_staging_batch(engine, staging_table: str, batch_id: int) -> None:
    """
    Delete existing rows for the same batch_id before reloading.
    This makes the ETL rerunnable.
    """

    schema_name, table_name = split_schema_table(staging_table)

    delete_sql = text(f"""
        DELETE FROM {schema_name}.{table_name}
        WHERE batch_id = :batch_id;
    """)

    with engine.begin() as connection:
        connection.execute(delete_sql, {"batch_id": batch_id})

    print(f"Cleared existing rows from {staging_table} for batch_id={batch_id}")


def prepare_dataframe_for_staging(
    df: pd.DataFrame,
    file_type: str,
    batch_id: int,
    target_columns: list[str],
) -> pd.DataFrame:
    """
    Prepare validated DataFrame for SQL staging load.
    """

    df = df.copy()

    column_mapping = get_column_mapping(file_type)

    existing_mapping = {
        source_col: target_col
        for source_col, target_col in column_mapping.items()
        if source_col in df.columns
    }

    df = df.rename(columns=existing_mapping)

    df["batch_id"] = batch_id

    if "source_file_name" not in df.columns:
        df["source_file_name"] = None

    if "source_row_number" not in df.columns:
        df["source_row_number"] = None

    if "is_valid" not in df.columns:
        df["is_valid"] = True

    if "validation_message" not in df.columns:
        df["validation_message"] = None

    for column in target_columns:
        if column not in df.columns:
            df[column] = None

    output_df = df[target_columns].copy()

    output_df = output_df.where(pd.notna(output_df), None)

    return output_df


def load_dataframe_to_staging(
    df: pd.DataFrame,
    file_type: str,
    batch_id: int,
    clear_existing_batch: bool = True,
) -> int:
    """
    Load one validated DataFrame into the correct SQL staging table.
    """

    if df.empty:
        print(f"No rows to load for file type: {file_type}")
        return 0

    config = get_file_config(file_type)
    staging_table = config["staging_table"]

    schema_name, table_name = split_schema_table(staging_table)

    engine = get_sql_engine()

    target_columns = get_target_columns(engine, staging_table)

    if clear_existing_batch:
        clear_staging_batch(engine, staging_table, batch_id)

    output_df = prepare_dataframe_for_staging(
        df=df,
        file_type=file_type,
        batch_id=batch_id,
        target_columns=target_columns,
    )

    output_df.to_sql(
        name=table_name,
        con=engine,
        schema=schema_name,
        if_exists="append",
        index=False,
        chunksize=1000,
    )

    rows_loaded = len(output_df)

    print(f"Loaded {rows_loaded} rows into {staging_table}")

    return rows_loaded