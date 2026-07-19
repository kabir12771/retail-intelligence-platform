from config.file_config import FILE_CONFIG, get_all_file_types, get_file_config
from config.column_mapping import COLUMN_MAPPING, get_column_mapping


def test_file_config():
    print("Testing FILE_CONFIG...")

    file_types = get_all_file_types()

    print(f"Total configured file types: {len(file_types)}")

    for file_type in file_types:
        config = get_file_config(file_type)

        print("-" * 60)
        print(f"File Type: {file_type}")
        print(f"Input Folder: {config['input_folder']}")
        print(f"Staging Table: {config['staging_table']}")
        print(f"File Pattern: {config['file_pattern']}")
        print(f"Required Columns: {config['required_columns']}")

    print("FILE_CONFIG test completed.")


def test_column_mapping():
    print("\nTesting COLUMN_MAPPING...")

    for file_type in COLUMN_MAPPING.keys():
        mapping = get_column_mapping(file_type)

        print("-" * 60)
        print(f"File Type: {file_type}")
        print(f"Mapped Columns: {len(mapping)}")

    print("COLUMN_MAPPING test completed.")


if __name__ == "__main__":
    test_file_config()
    test_column_mapping()