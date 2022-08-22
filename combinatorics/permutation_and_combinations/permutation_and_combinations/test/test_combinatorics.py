from hypothesis import given, strategies as st
import math

from permutation_and_combinations.combinatorics import factorial


@given(st.integers(min_value=10, max_value=100))
def test_factorial(end_range: int):
    fact = 1
    actual = factorial(fact, end_range)
    expect = math.factorial(end_range)
    assert actual == expect
