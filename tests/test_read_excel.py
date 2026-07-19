from extract.read_excel import get_excel_files, read_all_excel_files


if __name__ == "__main__":
    file_type = "product_master"

    files = get_excel_files(file_type)

    print(f"Files found for {file_type}: {len(files)}")

    for file in files:
        print(file)

    df = read_all_excel_files(file_type)

    print("\nPreview:")
    print(df.head())