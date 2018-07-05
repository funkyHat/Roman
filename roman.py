#!/usr/bin/env python3.6

expansions = {
    'IV': 'IIII',
    'IX': 'VIIII',
}


class Number:
    def __init__(self, value):
        self._value = self.normalize(value)

    def __add__(self, y):
        return Number(self._value + y._value)

    def __repr__(self):
        return f"Number('{self._value}')"

    def __eq__(self, y):
        return self._value == y._value

    def normalize(self, number):
        previous = None
        while previous != number:
            previous = number
            for old, new in expansions.items():
                number = number.replace(old, new, 1)
        order = "IVXLCDM"[::-1]
        number = ''.join(sorted(number, key=order.index))
        return number


def test_simple_add():
    x = Number('I')
    y = Number('I')
    assert x + y == Number('II')


def test_nasty_add():
    result = Number('III') + Number('I')
    assert result == Number('IV')


def test_another_add():
    result = Number('V') + Number('X')
    assert result == Number('XV')


def test_nice_repr():
    num = Number('IIII')
    assert repr(num) == "Number('IV')"
