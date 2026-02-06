from src.math_utils import add, sub, mul, div


def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(2, 1) == 3


def test_subtract():
    assert sub(1, 2) == -1
    assert sub(1, 1) == 0


def test_mul():
    assert mul(2, 2) == 4
    assert mul(-2, -2) == 4
    assert mul(2, -2) == -4
    assert mul(2, 0) == 0


def test_div():
    assert div(2, 2) == 1
