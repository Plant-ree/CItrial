# Your testing code
from src.my_math import *

def test_add_numbers():
    result = add_numbers(2, 5)
    assert result == 7

def test_subtract_numbers():
    result = subtract_numbers(2, 5)
    assert result == 3

def test_multiply_numbers():
    result = multiply_numbers(2, 5)
    assert result == 10
