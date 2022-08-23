from hypothesis import given, strategies as st
import math
import pytest

from permutation_and_combinations.combinatorics import combination, factorial, permutation


@given(st.integers(min_value=10, max_value=100))
def test_factorial(n: int):
    actual = factorial(n)
    expect = math.factorial(n)

    assert actual == expect


def test_both_negative_factorial_negative_end_range():
    n = -1

    with pytest.raises(ValueError):
        factorial(n)


def test_nonint_factorial_negative_end_range():
    n = "10"

    with pytest.raises(ValueError):
        factorial(n)


@given(st.integers(min_value=10, max_value=100), st.integers(min_value=2, max_value=5))
def test_permutation(n: int, r: int):
    actual = permutation(n, r)
    expect = math.perm(n, r)

    assert actual == expect


@given(st.integers(min_value=10, max_value=100), st.integers(min_value=2, max_value=5))
def test_combination(n: int, r: int):
    actual = combination(n, r)
    expect = math.comb(n, r)

    assert actual == expect

