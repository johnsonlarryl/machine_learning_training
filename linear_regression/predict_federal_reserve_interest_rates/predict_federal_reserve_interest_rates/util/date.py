import pandas as pd
from pandas import Period
import re


def parse_cpi_index_date(year: int, period: str) -> Period:
    try:
        month = get_month(period)
        return pd.Period(year=year, month=month, freq='M')
    except RuntimeError as e:
        raise e


def get_month(period):
    return int(re.search(r"M(\d{2})", period).group(1))
