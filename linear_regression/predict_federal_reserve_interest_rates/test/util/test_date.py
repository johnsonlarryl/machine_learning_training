import datetime
import os
import pandas as pd
from hypothesis import given, strategies as st
from predict_federal_reserve_interest_rates.util.date import get_month, parse_cpi_index_date

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def period_strategy() -> str:
    periods_df = pd.read_csv(f"{ROOT_DIR}/../../predict_federal_reserve_interest_rates/data/bls/cpi/bls_cpi_period.txt",
                             delim_whitespace=True)

    return st.lists(st.sampled_from(periods_df["period"].to_list()), min_size=1).map(",".join)


def get_year():
    return datetime.datetime.now().year


@given(st.integers(min_value=1929, max_value=get_year()),
       period_strategy())
def test_parse_cpi_index_date(year, period):
    month = get_month(period)
    expect_period = pd.Period(year=year, month=month, freq='M')
    actual_period = parse_cpi_index_date(year, period)
    assert expect_period == actual_period


