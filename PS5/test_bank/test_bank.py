import pytest
from bank import value

def test_0():
    assert value("Hello") == 0
    assert value("hello") == 0


def test_20():
    assert value("How") == 20
    assert value("how") == 20
    assert value("hi") == 20


def test_100():
    assert value("sir") == 100
    assert value("what' up") == 100