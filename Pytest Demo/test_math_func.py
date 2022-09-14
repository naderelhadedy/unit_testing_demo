import math_func
import pytest


# @pytest.mark.skip(reason="SHUT DOWN THIS TEST")
@pytest.mark.number
def test_add():
    assert math_func.add(5, 2) == 7
    assert math_func.add(3, 2) == 5
    assert math_func.add(0, 2) == 2
    assert math_func.add(-2, 2) == 0


@pytest.mark.number
def test_multiply():
    assert math_func.multiply(5, 2) == 10
    assert math_func.multiply(7, 2) == 14
    assert math_func.multiply(-2, 2) == -4
    assert math_func.multiply(0, 2) == 0


@pytest.mark.number
def test_divide():
    assert math_func.divide(4, 2) == 2
    assert math_func.divide(2, 2) == 1
    assert math_func.divide(4, -2) == -2
    assert math_func.divide(-16, 8) == -2
    assert math_func.divide(-24, -8) == 3
    assert math_func.divide(0, 3) == 0
    

@pytest.mark.string
def test_add_string():
    result =  math_func.add_string('Hello ', 'Ahmed')
    assert result == "Hello Ahmed"
    assert type(result) is str
    assert "Ahmed" in result


@pytest.mark.string
def test_multiply_string():
    assert math_func.multiply_string('HA', 3) == "HAHAHA"
    assert math_func.multiply_string('He ', 4) == "He He He He "


# parameterized tests
@pytest.mark.parametrize('var1, var2, result', 
                            [
                                (5, 7, 12), # int
                                ('Hello', ' World!', "Hello World!"), # str
                                (5.5, 8.5, 14.0) # float
                            ]
                        )
def test_add_any_type(var1, var2, result):
    assert math_func.add_any_type(var1, var2) == result
