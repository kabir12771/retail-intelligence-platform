from config.file_config import get_all_file_types
from extract.read_excel import read_all_excel_files
from validate.schema_validation import validate_schema


if __name__ == "__main__":
    file_types = get_all_file_types()

    for file_type in file_types:
        print("=" * 80)
        print(f"Testing schema validation for: {file_type}")

        df = read_all_excel_files(file_type)

        result = validate_schema(df, file_type)

        print(f"File Type: {result.file_type}")
        print(f"Is Valid: {result.is_valid}")
        print(f"Total Rows: {result.total_rows}")
        print(f"Invalid Rows: {result.invalid_rows}")
        print(f"Missing Columns: {result.missing_columns}")

        if result.invalid_rows > 0:
            print("\nInvalid Rows Preview:")
            print(
                result.dataframe[
                    result.dataframe["is_valid"] == False
                ][["source_file_name", "source_row_number", "validation_message"]]
            )
        else:
            print("Schema validation passed.")