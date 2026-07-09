import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def load_csv(file_name: str) -> pd.DataFrame:
    path = RAW_DATA_PATH / file_name
    return pd.read_csv(path)


def validate_required_columns(df: pd.DataFrame, required_columns: list[str], table_name: str) -> None:
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"{table_name} missing columns: {missing}")


def clean_sales() -> pd.DataFrame:
    df = load_csv("sales_sample.csv")

    required_columns = [
        "date", "brand", "store_code", "item_no", "style",
        "season", "qty", "unit_price", "sales_value"
    ]
    validate_required_columns(df, required_columns, "sales_sample")

    df["date"] = pd.to_datetime(df["date"])
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce").fillna(0)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)
    df["sales_value"] = df["qty"] * df["unit_price"]

    return df


def main() -> None:
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    sales = clean_sales()
    output_path = PROCESSED_DATA_PATH / "sales_clean.csv"
    sales.to_csv(output_path, index=False)

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
