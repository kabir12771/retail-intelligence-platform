from datetime import datetime
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = BASE_DIR / "reports"


def auto_adjust_excel_columns(writer, sheet_name: str, df: pd.DataFrame) -> None:
    """
    Auto-adjust Excel column widths safely.
    """

    worksheet = writer.sheets[sheet_name]

    for column_index, column_name in enumerate(df.columns):
        try:
            column_values = df.iloc[:, column_index]

            value_lengths = column_values.apply(
                lambda value: len(str(value)) if pd.notna(value) else 0
            )

            max_value_length = int(value_lengths.max()) if not value_lengths.empty else 0
            header_length = len(str(column_name))

            adjusted_width = min(
                max(max_value_length, header_length) + 2,
                70,
            )

            worksheet.set_column(
                column_index,
                column_index,
                adjusted_width,
            )

        except Exception:
            worksheet.set_column(
                column_index,
                column_index,
                20,
            )


def build_run_summary_dataframe(
    batch_id: int,
    pipeline_name: str,
    pipeline_status: str,
    started_at: datetime,
    completed_at: datetime,
    results: list[dict],
    log_file_path,
    summary_report_path,
) -> pd.DataFrame:
    """
    Build one-row run summary.
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

    no_file_types = sum(
        1 for result in results
        if result["status"] == "NO_FILE"
    )

    duration_seconds = round(
        (completed_at - started_at).total_seconds(),
        2,
    )

    return pd.DataFrame(
        [
            {
                "batch_id": batch_id,
                "pipeline_name": pipeline_name,
                "pipeline_status": pipeline_status,
                "started_at": started_at.strftime("%Y-%m-%d %H:%M:%S"),
                "completed_at": completed_at.strftime("%Y-%m-%d %H:%M:%S"),
                "duration_seconds": duration_seconds,
                "total_file_types": len(results),
                "successful_file_types": successful_file_types,
                "failed_file_types": failed_file_types,
                "no_file_types": no_file_types,
                "total_rows_read": total_rows_read,
                "total_rows_loaded": total_rows_loaded,
                "log_file_path": str(log_file_path),
                "summary_report_path": str(summary_report_path),
            }
        ]
    )


def build_file_results_dataframe(results: list[dict]) -> pd.DataFrame:
    """
    Build file-level result table.
    """

    file_rows = []

    for result in results:
        started_at = result.get("started_at")
        completed_at = result.get("completed_at")

        duration_seconds = None

        if started_at and completed_at:
            duration_seconds = round(
                (completed_at - started_at).total_seconds(),
                2,
            )

        file_rows.append(
            {
                "file_type": result.get("file_type"),
                "status": result.get("status"),
                "rows_read": result.get("rows_read"),
                "rows_loaded": result.get("rows_loaded"),
                "invalid_rows": result.get("invalid_rows"),
                "started_at": started_at.strftime("%Y-%m-%d %H:%M:%S") if started_at else None,
                "completed_at": completed_at.strftime("%Y-%m-%d %H:%M:%S") if completed_at else None,
                "duration_seconds": duration_seconds,
                "message": result.get("message"),
                "error_report_path": result.get("error_report_path"),
            }
        )

    return pd.DataFrame(file_rows)


def build_validation_dataframe(validation_results: list[dict]) -> pd.DataFrame:
    """
    Build post-load validation result table.
    """

    if not validation_results:
        return pd.DataFrame(
            [
                {
                    "check_name": "Post-load validation",
                    "object_name": None,
                    "expected": None,
                    "actual": None,
                    "passed": None,
                    "message": "Post-load validation was not executed.",
                }
            ]
        )

    return pd.DataFrame(validation_results)


def build_runtime_config_dataframe(runtime_config: dict) -> pd.DataFrame:
    """
    Convert runtime config dictionary into a two-column table.
    """

    rows = []

    for key, value in runtime_config.items():
        rows.append(
            {
                "config_key": key,
                "config_value": value,
            }
        )

    return pd.DataFrame(rows)


def export_pipeline_run_summary(
    batch_id: int,
    pipeline_name: str,
    pipeline_status: str,
    started_at: datetime,
    completed_at: datetime,
    results: list[dict],
    validation_results: list[dict],
    runtime_config: dict,
    log_file_path,
) -> str:
    """
    Export full ETL run summary to Excel.
    """

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = completed_at.strftime("%Y%m%d_%H%M%S")

    summary_report_path = (
        REPORTS_DIR
        / f"{batch_id}_{timestamp}_etl_run_summary.xlsx"
    )

    run_summary_df = build_run_summary_dataframe(
        batch_id=batch_id,
        pipeline_name=pipeline_name,
        pipeline_status=pipeline_status,
        started_at=started_at,
        completed_at=completed_at,
        results=results,
        log_file_path=log_file_path,
        summary_report_path=summary_report_path,
    )

    file_results_df = build_file_results_dataframe(results)
    validation_df = build_validation_dataframe(validation_results)
    runtime_config_df = build_runtime_config_dataframe(runtime_config)

    with pd.ExcelWriter(summary_report_path, engine="xlsxwriter") as writer:
        run_summary_df.to_excel(
            writer,
            sheet_name="Run_Summary",
            index=False,
        )

        file_results_df.to_excel(
            writer,
            sheet_name="File_Results",
            index=False,
        )

        validation_df.to_excel(
            writer,
            sheet_name="Post_Load_Validation",
            index=False,
        )

        runtime_config_df.to_excel(
            writer,
            sheet_name="Runtime_Config",
            index=False,
        )

        auto_adjust_excel_columns(writer, "Run_Summary", run_summary_df)
        auto_adjust_excel_columns(writer, "File_Results", file_results_df)
        auto_adjust_excel_columns(writer, "Post_Load_Validation", validation_df)
        auto_adjust_excel_columns(writer, "Runtime_Config", runtime_config_df)

    print(f"Pipeline run summary report exported: {summary_report_path}")

    return str(summary_report_path)