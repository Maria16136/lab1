import pytest

from src.toolkit.calculator import calc


# положительные тесты
def test_calculation():
    assert calc('2+3') == 5


def test_priority_operation():
    assert calc('10+5*12') == 70


def test_mix_operation():
    assert calc('20-5*2+20/2+4') == 24


def test_fractional_numbers():
    assert calc('0.2+1.25') == 1.45


def test_unary_minus():
    assert calc('-5+15') == 10


def test_mix_unary_symbols():
    assert calc('+12*-2') == -24


def test_ignore_spaces():
    assert calc('7 +4 * 5') == 27


def test_mix_conditions():
    assert calc('-20 / -2 * +0.1 - 0 + +12') == 13


# отрицательные тесты
def test_ends_with_sign():
    with pytest.raises(ValueError):
        calc('2+')


def test_consecutive_operators():
    with pytest.raises(ValueError):
        calc('10+*2')


def test_division_by_zero():
    with pytest.raises(ValueError):
        calc('5/0')


def test_division_by_fraction_zero():
    with pytest.raises(ValueError):
        calc('10/0.0')


def test_empty_string():
    with pytest.raises(ValueError):
        calc('')


def test_invalid_characters():
    with pytest.raises(ValueError):
        calc('7+a')


def test_invalid_sign():
    with pytest.raises(ValueError):
        calc('10%3')


def test_leading_zero():
    with pytest.raises(ValueError):
        calc('015+1')