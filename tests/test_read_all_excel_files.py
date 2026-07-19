from config.file_config import get_all_file_types
from extract.read_excel import read_all_excel_files


if __name__ == "__main__":
    file_types = get_all_file_types()

    for file_type in file_types:
        print("=" * 80)
        print(f"Testing file type: {file_type}")

        df = read_all_excel_files(file_type)

        print(f"Rows read: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        print(df.head())