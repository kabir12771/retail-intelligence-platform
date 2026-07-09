import pandas as pd
from python.src.kpi_calculations import calculate_wape, calculate_bias


def test_calculate_wape():
    actual = pd.Series([100, 200])
    forecast = pd.Series([90, 220])

    result = calculate_wape(actual, forecast)

    assert round(result, 4) == 0.1


def test_calculate_bias():
    actual = pd.Series([100, 200])
    forecast = pd.Series([90, 220])

    result = calculate_bias(actual, forecast)

    assert round(result, 4) == 0.0333
