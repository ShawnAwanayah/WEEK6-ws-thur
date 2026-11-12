import pytest
from main import add_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3


def test_add_numbers_2():
    assert add_numbers(1, 3) == 4
