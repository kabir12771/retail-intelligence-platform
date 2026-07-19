from pathlib import Path
import pandas as pd

from config.file_config import get_file_config


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize Excel column names:
    - strip spaces
    - lowercase
    - replace spaces with underscores
    - remove special line breaks
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("\n", "_", regex=False)
        .str.replace("\r", "_", regex=False)
    )

    return df


def get_excel_files(file_type: str) -> list[Path]:
    """
    Return all Excel files for a configured file type.
    """

    config = get_file_config(file_type)
    input_folder = config["input_folder"]
    file_pattern = config["file_pattern"]

    input_folder.mkdir(parents=True, exist_ok=True)

    files = list(input_folder.glob(file_pattern))

    return files


def read_excel_file(file_path: Path, file_type: str) -> pd.DataFrame:
    """
    Read one Excel file and add metadata columns.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_excel(file_path)

    df = standardize_column_names(df)

    df.insert(0, "source_row_number", range(1, len(df) + 1))
    df.insert(0, "source_file_name", file_path.name)

    print(f"Read file successfully: {file_path.name}")
    print(f"File type: {file_type}")
    print(f"Rows read: {len(df)}")
    print(f"Columns found: {list(df.columns)}")

    return df


def read_all_excel_files(file_type: str) -> pd.DataFrame:
    """
    Read all Excel files for one file type and combine them.
    """

    files = get_excel_files(file_type)

    if not files:
        print(f"No files found for file type: {file_type}")
        return pd.DataFrame()

    dataframes = []

    for file_path in files:
        df = read_excel_file(file_path, file_type)
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)

    print("-" * 60)
    print(f"Combined file type: {file_type}")
    print(f"Total files read: {len(files)}")
    print(f"Total rows read: {len(combined_df)}")

    return combined_df