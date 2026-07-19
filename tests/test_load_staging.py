from config.file_config import get_all_file_types
from extract.read_excel import read_all_excel_files
from validate.schema_validation import validate_schema
from validate.data_quality_checks import run_data_quality_checks
from load.staging_loader import load_dataframe_to_staging


BATCH_ID = 2001


if __name__ == "__main__":
    file_types = get_all_file_types()

    total_rows_loaded = 0

    for file_type in file_types:
        print("=" * 80)
        print(f"Processing file type: {file_type}")

        df = read_all_excel_files(file_type)

        schema_result = validate_schema(df, file_type)

        if not schema_result.is_valid:
            print(f"Schema validation failed for {file_type}. Skipping load.")
            continue

        dq_result = run_data_quality_checks(
            schema_result.dataframe,
            file_type,
        )

        if not dq_result.is_valid:
            print(f"Data quality validation failed for {file_type}. Skipping load.")
            continue

        rows_loaded = load_dataframe_to_staging(
            df=dq_result.dataframe,
            file_type=file_type,
            batch_id=BATCH_ID,
            clear_existing_batch=True,
        )

        total_rows_loaded += rows_loaded

    print("=" * 80)
    print(f"Total rows loaded to staging: {total_rows_loaded}")