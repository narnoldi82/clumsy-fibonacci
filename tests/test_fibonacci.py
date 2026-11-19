"""Tests for the Fibonacci series generator."""
import pytest
from fibonacci import print_fibonacci_series


def test_empty_series():
    assert print_fibonacci_series(0) == []


def test_single_element():
    assert print_fibonacci_series(1) == [0]


def test_two_elements():
    assert print_fibonacci_series(2) == [0, 1]


def test_first_ten():
    assert print_fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_type_error_for_float():
    with pytest.raises(TypeError):
        print_fibonacci_series(3.0)


def test_type_error_for_string():
    with pytest.raises(TypeError):
        print_fibonacci_series("5")


def test_type_error_for_bool():
    with pytest.raises(TypeError):
        print_fibonacci_series(True)


def test_value_error_for_negative():
    with pytest.raises(ValueError):
        print_fibonacci_series(-1)
