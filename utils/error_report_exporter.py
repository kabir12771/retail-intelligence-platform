from datetime import datetime
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
ERROR_REPORT_DIR = BASE_DIR / "error_reports"


def get_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return invalid rows if is_valid exists.
    If is_valid does not exist, return full DataFrame.
    """

    if df is None or df.empty:
        return pd.DataFrame()

    if "is_valid" not in df.columns:
        return df.copy()

    invalid_df = df[df["is_valid"] == False].copy()

    return invalid_df


def auto_adjust_excel_columns(writer, sheet_name: str, df: pd.DataFrame) -> None:
    """
    Auto-adjust Excel column widths safely.
    Handles numbers, blanks, dates, pandas NA values, and mixed data types.
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
                60,
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


def export_error_report(
    batch_id: int,
    file_type: str,
    validation_stage: str,
    df: pd.DataFrame,
    message: str | None = None,
    missing_columns: list[str] | None = None,
) -> str | None:
    """
    Export validation errors to an Excel file.
    """

    ERROR_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    invalid_df = get_invalid_rows(df)

    if invalid_df.empty and not message and not missing_columns:
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = (
        ERROR_REPORT_DIR
        / f"{batch_id}_{file_type}_{validation_stage}_{timestamp}_error_report.xlsx"
    )

    summary_df = pd.DataFrame(
        [
            {
                "batch_id": batch_id,
                "file_type": file_type,
                "validation_stage": validation_stage,
                "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "rejected_rows": len(invalid_df),
                "missing_columns": ", ".join(missing_columns or []),
                "message": message,
            }
        ]
    )

    if invalid_df.empty:
        invalid_df = pd.DataFrame(
            [
                {
                    "file_type": file_type,
                    "validation_stage": validation_stage,
                    "message": message,
                    "missing_columns": ", ".join(missing_columns or []),
                }
            ]
        )

    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False,
        )

        invalid_df.to_excel(
            writer,
            sheet_name="Rejected_Rows",
            index=False,
        )

        auto_adjust_excel_columns(
            writer=writer,
            sheet_name="Summary",
            df=summary_df,
        )

        auto_adjust_excel_columns(
            writer=writer,
            sheet_name="Rejected_Rows",
            df=invalid_df,
        )

    print(f"Error report exported: {output_file}")

    return str(output_file)