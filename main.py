from datetime import datetime

from config.file_config import get_all_file_types
from config.pipeline_config import (
    build_expected_fact_counts_from_results,
)
from extract.read_excel import read_all_excel_files
from validate.schema_validation import validate_schema
from validate.data_quality_checks import run_data_quality_checks
from validate.post_load_validation import (
    run_post_load_validation,
    print_validation_results,
)
from load.staging_loader import load_dataframe_to_staging
from load.dw_loader import (
    execute_all_dw_load_procedures,
    print_dw_batch_row_counts,
)
from audit.audit_logger import (
    start_batch_log,
    complete_batch_log,
    log_file_result,
    log_data_quality_errors,
)
from utils.error_report_exporter import export_error_report
from utils.file_mover import move_files_after_pipeline
from utils.cli_args import (
    parse_cli_args,
    build_effective_runtime_config,
    print_effective_runtime_config,
)
from utils.pipeline_logger import (
    create_log_file_path,
    configure_python_logger,
    PipelineLogCapture,
    print_log_header,
    print_log_footer,
)
from utils.run_summary_report import export_pipeline_run_summary


def generate_batch_id() -> int:
    """
    Generate SQL Server INT-safe batch id.
    Format: YY + day-of-year + HHMM
    Example: 261931545
    """

    return int(datetime.now().strftime("%y%j%H%M"))


def process_file_type(
    file_type: str,
    batch_id: int,
    runtime_config: dict,
) -> dict:
    """
    Process one file type:
    - read Excel files
    - validate schema
    - run data quality checks
    - export error report if rejected
    - load valid rows to staging
    - log file result
    """

    started_at = datetime.now()

    print("=" * 80)
    print(f"Processing file type: {file_type}")
    print("=" * 80)

    result = {
        "file_type": file_type,
        "status": "NOT_STARTED",
        "rows_read": 0,
        "rows_loaded": 0,
        "invalid_rows": 0,
        "message": None,
        "error_report_path": None,
        "started_at": started_at,
        "completed_at": None,
    }

    try:
        df = read_all_excel_files(file_type)

        if df.empty:
            result["status"] = "NO_FILE"
            result["message"] = "No source file found."
            print(f"No source file found for {file_type}.")
            return result

        result["rows_read"] = len(df)

        schema_result = validate_schema(df, file_type)

        if not schema_result.is_valid:
            result["status"] = "SCHEMA_FAILED"
            result["invalid_rows"] = schema_result.invalid_rows
            result["message"] = (
                f"Schema validation failed. Missing columns: "
                f"{schema_result.missing_columns}"
            )

            print(result["message"])

            error_report_path = export_error_report(
                batch_id=batch_id,
                file_type=file_type,
                validation_stage="SCHEMA_FAILED",
                df=schema_result.dataframe,
                message=result["message"],
                missing_columns=schema_result.missing_columns,
            )

            result["error_report_path"] = error_report_path

            if error_report_path:
                result["message"] = (
                    f"{result['message']} Error report: {error_report_path}"
                )

            log_data_quality_errors(
                batch_id=batch_id,
                file_type=file_type,
                df=schema_result.dataframe,
            )

            return result

        dq_result = run_data_quality_checks(
            schema_result.dataframe,
            file_type,
        )

        if not dq_result.is_valid:
            result["status"] = "DATA_QUALITY_FAILED"
            result["invalid_rows"] = dq_result.invalid_rows
            result["message"] = "Data quality validation failed."

            print(result["message"])
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

            error_report_path = export_error_report(
                batch_id=batch_id,
                file_type=file_type,
                validation_stage="DATA_QUALITY_FAILED",
                df=dq_result.dataframe,
                message=result["message"],
                missing_columns=None,
            )

            result["error_report_path"] = error_report_path

            if error_report_path:
                result["message"] = (
                    f"{result['message']} Error report: {error_report_path}"
                )

            log_data_quality_errors(
                batch_id=batch_id,
                file_type=file_type,
                df=dq_result.dataframe,
            )

            return result

        rows_loaded = load_dataframe_to_staging(
            df=dq_result.dataframe,
            file_type=file_type,
            batch_id=batch_id,
            clear_existing_batch=runtime_config["CLEAR_STAGING_BATCH"],
        )

        result["status"] = "SUCCESS"
        result["rows_loaded"] = rows_loaded
        result["message"] = "Loaded successfully."

        return result

    except Exception as error:
        result["status"] = "FAILED"
        result["message"] = str(error)

        print(f"Error while processing {file_type}: {error}")

        error_report_path = export_error_report(
            batch_id=batch_id,
            file_type=file_type,
            validation_stage="FAILED",
            df=df if "df" in locals() else None,
            message=str(error),
            missing_columns=None,
        )

        result["error_report_path"] = error_report_path

        if error_report_path:
            result["message"] = (
                f"{result['message']} Error report: {error_report_path}"
            )

        return result

    finally:
        result["completed_at"] = datetime.now()

        try:
            log_file_result(
                batch_id=batch_id,
                result=result,
            )
        except Exception as audit_error:
            print(
                f"Warning: failed to write file audit log for {file_type}: "
                f"{audit_error}"
            )


def calculate_summary_numbers(results: list[dict]) -> dict:
    """
    Calculate pipeline summary numbers.
    """

    total_rows_read = sum(result["rows_read"] for result in results)
    total_rows_loaded = sum(result["rows_loaded"] for result in results)

    successful_file_types = sum(
        1 for result in results
        if result["status"] == "SUCCESS"
    )

    failed_file_types = sum(
        1 for result in results
        if result["status"] not in ["SUCCESS", "NO_FILE"]
    )

    return {
        "total_rows_read": total_rows_read,
        "total_rows_loaded": total_rows_loaded,
        "successful_file_types": successful_file_types,
        "failed_file_types": failed_file_types,
    }


def print_pipeline_summary(results: list[dict], batch_id: int) -> None:
    """
    Print final ETL summary.
    """

    summary = calculate_summary_numbers(results)

    print("=" * 80)
    print(f"ETL PIPELINE SUMMARY - BATCH ID: {batch_id}")
    print("=" * 80)

    for result in results:
        print(
            f"{result['file_type']:<25} "
            f"Status: {result['status']:<20} "
            f"Rows Read: {result['rows_read']:<5} "
            f"Rows Loaded: {result['rows_loaded']:<5} "
            f"Invalid Rows: {result['invalid_rows']:<5}"
        )

        if result["message"]:
            print(f"  Message: {result['message']}")

        if result.get("error_report_path"):
            print(f"  Error Report: {result['error_report_path']}")

    print("-" * 80)
    print(f"Total Rows Read: {summary['total_rows_read']}")
    print(f"Total Rows Loaded to Staging: {summary['total_rows_loaded']}")
    print(f"Successful File Types: {summary['successful_file_types']}")
    print(f"Failed File Types: {summary['failed_file_types']}")
    print("=" * 80)


def export_summary_report_safe(
    batch_id: int,
    pipeline_status: str,
    pipeline_started_at: datetime,
    results: list[dict],
    validation_results: list[dict],
    runtime_config: dict,
    log_file_path,
) -> str:
    """
    Export pipeline run summary report.
    """

    pipeline_completed_at = datetime.now()

    summary_report_path = export_pipeline_run_summary(
        batch_id=batch_id,
        pipeline_name=runtime_config["PIPELINE_NAME"],
        pipeline_status=pipeline_status,
        started_at=pipeline_started_at,
        completed_at=pipeline_completed_at,
        results=results,
        validation_results=validation_results,
        runtime_config=runtime_config,
        log_file_path=log_file_path,
    )

    return summary_report_path


def main() -> None:
    """
    Main ETL runner.
    """

    args = parse_cli_args()
    runtime_config = build_effective_runtime_config(args)

    batch_id = runtime_config["CLI_BATCH_ID"] or generate_batch_id()

    log_file_path = create_log_file_path(batch_id)

    logger = configure_python_logger(
        batch_id=batch_id,
        log_file_path=log_file_path,
    )

    file_types = get_all_file_types()
    results = []
    validation_results = []
    pipeline_started_at = datetime.now()

    with PipelineLogCapture(log_file_path):
        print_log_header(
            batch_id=batch_id,
            log_file_path=log_file_path,
        )

        logger.info("ETL run started.")

        print("=" * 80)
        print("Retail Intelligence Platform - Python ETL Runner")
        print("=" * 80)
        print(f"Batch ID: {batch_id}")
        print(f"Started At: {datetime.now()}")
        print("=" * 80)

        print_effective_runtime_config(runtime_config)

        try:
            start_batch_log(
                batch_id=batch_id,
                pipeline_name=runtime_config["PIPELINE_NAME"],
                total_file_types=len(file_types),
            )

            for file_type in file_types:
                result = process_file_type(
                    file_type=file_type,
                    batch_id=batch_id,
                    runtime_config=runtime_config,
                )

                results.append(result)

            print_pipeline_summary(
                results=results,
                batch_id=batch_id,
            )

            summary = calculate_summary_numbers(results)

            failed_results = [
                result for result in results
                if result["status"] not in ["SUCCESS", "NO_FILE"]
            ]

            if failed_results:
                if runtime_config["MOVE_REJECTED_FILES_ON_FAILURE"]:
                    move_files_after_pipeline(
                        results=results,
                        batch_id=batch_id,
                        pipeline_success=False,
                    )
                else:
                    print("Rejected file movement skipped by configuration or CLI argument.")

                complete_batch_log(
                    batch_id=batch_id,
                    batch_status="FAILED",
                    successful_file_types=summary["successful_file_types"],
                    failed_file_types=summary["failed_file_types"],
                    total_rows_read=summary["total_rows_read"],
                    total_rows_loaded=summary["total_rows_loaded"],
                    error_message="One or more file types failed validation or loading.",
                )

                summary_report_path = export_summary_report_safe(
                    batch_id=batch_id,
                    pipeline_status="FAILED",
                    pipeline_started_at=pipeline_started_at,
                    results=results,
                    validation_results=validation_results,
                    runtime_config=runtime_config,
                    log_file_path=log_file_path,
                )

                print("ETL stopped because one or more file types failed validation/loading.")
                print("Fix the failed source files first, then rerun main.py.")
                print(f"Summary Report: {summary_report_path}")

                logger.error("ETL stopped because one or more file types failed.")
                print_log_footer(log_file_path)
                return

            successful_loads = [
                result for result in results
                if result["status"] == "SUCCESS"
            ]

            if not successful_loads:
                complete_batch_log(
                    batch_id=batch_id,
                    batch_status="NO_DATA",
                    successful_file_types=summary["successful_file_types"],
                    failed_file_types=summary["failed_file_types"],
                    total_rows_read=summary["total_rows_read"],
                    total_rows_loaded=summary["total_rows_loaded"],
                    error_message="No files were loaded to staging.",
                )

                summary_report_path = export_summary_report_safe(
                    batch_id=batch_id,
                    pipeline_status="NO_DATA",
                    pipeline_started_at=pipeline_started_at,
                    results=results,
                    validation_results=validation_results,
                    runtime_config=runtime_config,
                    log_file_path=log_file_path,
                )

                print("No files were loaded to staging. DW procedures will not run.")
                print(f"Summary Report: {summary_report_path}")

                logger.warning("ETL finished with NO_DATA status.")
                print_log_footer(log_file_path)
                return

            execute_all_dw_load_procedures(batch_id=batch_id)
            print_dw_batch_row_counts(batch_id=batch_id)

            if runtime_config["ENABLE_POST_LOAD_VALIDATION"]:
                expected_fact_counts = build_expected_fact_counts_from_results(results)

                validation_results = run_post_load_validation(
                    batch_id=batch_id,
                    expected_fact_counts=expected_fact_counts,
                    expected_batch_status="RUNNING",
                    expected_file_log_count=len(file_types),
                    validate_mart_views=runtime_config["VALIDATE_MART_VIEWS"],
                )

                print_validation_results(validation_results)

            else:
                print("Post-load validation skipped by configuration or CLI argument.")

            if runtime_config["MOVE_FILES_AFTER_SUCCESS"]:
                move_files_after_pipeline(
                    results=results,
                    batch_id=batch_id,
                    pipeline_success=True,
                )
            else:
                print("Processed file movement skipped by configuration or CLI argument.")

            complete_batch_log(
                batch_id=batch_id,
                batch_status="SUCCESS",
                successful_file_types=summary["successful_file_types"],
                failed_file_types=summary["failed_file_types"],
                total_rows_read=summary["total_rows_read"],
                total_rows_loaded=summary["total_rows_loaded"],
                error_message=None,
            )

            summary_report_path = export_summary_report_safe(
                batch_id=batch_id,
                pipeline_status="SUCCESS",
                pipeline_started_at=pipeline_started_at,
                results=results,
                validation_results=validation_results,
                runtime_config=runtime_config,
                log_file_path=log_file_path,
            )

            print("=" * 80)
            print("ETL pipeline completed successfully.")
            print(f"Summary Report: {summary_report_path}")

            if runtime_config["ENABLE_POST_LOAD_VALIDATION"]:
                print("Post-load validation passed.")

            if runtime_config["MOVE_FILES_AFTER_SUCCESS"]:
                print("Successful source files were moved to processed_files.")
            else:
                print("Successful source files were left in input_files.")

            print(f"Completed At: {datetime.now()}")
            print("=" * 80)

            logger.info("ETL run completed successfully.")
            print_log_footer(log_file_path)

        except Exception as error:
            summary = calculate_summary_numbers(results)

            try:
                complete_batch_log(
                    batch_id=batch_id,
                    batch_status="FAILED",
                    successful_file_types=summary["successful_file_types"],
                    failed_file_types=summary["failed_file_types"],
                    total_rows_read=summary["total_rows_read"],
                    total_rows_loaded=summary["total_rows_loaded"],
                    error_message=str(error),
                )
            except Exception as audit_error:
                print(f"Warning: failed to update batch audit log: {audit_error}")

            logger.exception("ETL pipeline failed.")

            try:
                summary_report_path = export_summary_report_safe(
                    batch_id=batch_id,
                    pipeline_status="FAILED",
                    pipeline_started_at=pipeline_started_at,
                    results=results,
                    validation_results=validation_results,
                    runtime_config=runtime_config,
                    log_file_path=log_file_path,
                )
            except Exception as report_error:
                summary_report_path = None
                print(f"Warning: failed to export summary report: {report_error}")

            print("=" * 80)
            print("ETL pipeline failed.")
            print(f"Error: {error}")
            print("Source files were not moved to processed_files.")

            if summary_report_path:
                print(f"Summary Report: {summary_report_path}")

            print("=" * 80)

            print_log_footer(log_file_path)

            raise


if __name__ == "__main__":
    main()