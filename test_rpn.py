import pytest

import rpn


def test_add():
    result = rpn.calculate("1 1 +")
    assert 2 == result
def test_subtract():
    result = rpn.calculate("5 3 -")
    assert 2 == result
def test_multiply():
    result = rpn.calculate("5 3 *")
    assert 15 == result
def test_divide():
    result = rpn.calculate("6 3 /")
    assert 2 == result
def test_exponent():
    result = rpn.calculate("4 3 ^")
    assert 64 == result

