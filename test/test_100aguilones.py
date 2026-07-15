import pytest
from calc.calc import add, multiply

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1.5, 2.5, 4.0),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (1.5, 2.5, 3.75),
    (-1, 1, -1),
    (0, 0, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected