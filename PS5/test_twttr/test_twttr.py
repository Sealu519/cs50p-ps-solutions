import pytest
from twttr import shorten


def test1():
    assert shorten("aeiou") == ""
    assert shorten("1a") == "1"
    assert shorten("sdf") == "sdf"
