import pytest
import math

def test_new_test():
    assert True

@pytest.fixture
def input_value():
    input = 5
    return input

def test_math_sqrt(input_value):
    x = input_value
    assert x * x == 25


@pytest.mark.math
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_item_in_list():
    assert 777 in [item for item in [111, 222, 777, 555]]