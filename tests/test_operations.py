from src.math_operations import add, subtract

# src/test_math_operations.py

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_positive_and_negative():
    assert add(5, -2) == 3

def test_add_zeros():
    assert add(0, 0) == 0

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_positive_and_negative():
    assert subtract(5, -2) == 7

def test_subtract_zeros():
    assert subtract(0, 0) == 0