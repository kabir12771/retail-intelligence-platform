from config.file_config import get_all_file_types
from extract.read_excel import read_all_excel_files
from validate.schema_validation import validate_schema
from validate.data_quality_checks import run_data_quality_checks


if __name__ == "__main__":
    file_types = get_all_file_types()

    for file_type in file_types:
        print("=" * 80)
        print(f"Testing data quality checks for: {file_type}")

        df = read_all_excel_files(file_type)

        schema_result = validate_schema(df, file_type)

        if not schema_result.is_valid:
            print("Schema validation failed. Skipping data quality checks.")
            print(f"Missing Columns: {schema_result.missing_columns}")
            print(f"Invalid Rows: {schema_result.invalid_rows}")
            continue

        dq_result = run_data_quality_checks(
            schema_result.dataframe,
            file_type,
        )

        print(f"File Type: {dq_result.file_type}")
        print(f"Is Valid: {dq_result.is_valid}")
        print(f"Total Rows: {dq_result.total_rows}")
        print(f"Invalid Rows: {dq_result.invalid_rows}")

        if dq_result.invalid_rows > 0:
            print("\nInvalid Rows Preview:")
            print(
                dq_result.dataframe[
                    dq_result.dataframe["is_valid"] == False
                ][
                    [
                        "source_file_name",
                        "source_row_number",
                        "validation_message",
                    ]
                ]
            )
        else:
            print("Data quality checks passed.")