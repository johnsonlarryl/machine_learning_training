from hypothesis import given, strategies as st
import math
import pytest

from permutation_and_combinations.combinatorics import factorial


@given(st.integers(min_value=10, max_value=100))
def test_factorial(end_range: int):
    actual = factorial(end_range)
    expect = math.factorial(end_range)

    assert actual == expect


def test_both_negative_factorial_negative_end_range():
    end_range = -1

    with pytest.raises(ValueError):
        factorial(end_range)


def test_nonint_factorial_negative_end_range():
    end_range = "10"

    with pytest.raises(ValueError):
        factorial(end_range)
