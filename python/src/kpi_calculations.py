import pandas as pd


def calculate_wape(actual_qty: pd.Series, forecast_qty: pd.Series) -> float | None:
    total_actual = actual_qty.sum()
    if total_actual == 0:
        return None

    absolute_error = (actual_qty - forecast_qty).abs().sum()
    return absolute_error / total_actual


def calculate_bias(actual_qty: pd.Series, forecast_qty: pd.Series) -> float | None:
    total_actual = actual_qty.sum()
    if total_actual == 0:
        return None

    return (forecast_qty.sum() - actual_qty.sum()) / total_actual
