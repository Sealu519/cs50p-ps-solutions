import pytest
from numb3rs import validate


def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1000.0.0.0") == False
    assert validate("cat") == False
    assert validate("1.1") == False
    assert validate("0.0.0.0.0") == False
