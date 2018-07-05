#!/usr/bin/env python3.6

class Number:
    def __init__(self, value):
        self._value = value

    def __add__(self, y):
        return Number(self._value + y._value)

    def __repr__(self):
        return f"Number('{self._value}')"

    def __eq__(self, y):
        return self._value == y._value


def test_simple_add():
    x = Number('I')
    y = Number('I')
    assert x + y == Number('II')
