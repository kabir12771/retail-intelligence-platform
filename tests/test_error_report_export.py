from extract.read_excel import read_all_excel_files
from validate.schema_validation import validate_schema
from validate.data_quality_checks import run_data_quality_checks
from utils.error_report_exporter import export_error_report


BATCH_ID = 9999
FILE_TYPE = "product_master"


if __name__ == "__main__":
    df = read_all_excel_files(FILE_TYPE)

    # Convert numeric column to object so we can inject bad test data
    df["retail_price"] = df["retail_price"].astype("object")

    # Create a fake data quality issue
    df.loc[0, "retail_price"] = "wrong_price"

    schema_result = validate_schema(df, FILE_TYPE)

    dq_result = run_data_quality_checks(
        schema_result.dataframe,
        FILE_TYPE,
    )

    if dq_result.is_valid:
        print("Test failed: data quality issue was not detected.")
    else:
        print("Data quality issue detected successfully.")

        error_report_path = export_error_report(
            batch_id=BATCH_ID,
            file_type=FILE_TYPE,
            validation_stage="DATA_QUALITY_FAILED",
            df=dq_result.dataframe,
            message="Test error report export.",
            missing_columns=None,
        )

        print(f"Error report created: {error_report_path}")