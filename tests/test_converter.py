import pytest

from src.toolkit.converter import convert


# положительные тесты
def test_cm_to_m():
    assert convert('100', 'cm', 'm') == 1


def test_m_to_cm():
    assert convert('3', 'm', 'cm') == 300


def test_mm_to_km():
    assert convert('12000', 'mm', 'km') == 0.012


def test_same_length_units():
    assert convert('5', 'm', 'm') == 5


def test_g_to_kg():
    assert convert('2000', 'g', 'kg') == 2


def test_kg_to_g():
    assert convert('0.5', 'kg', 'g') == 500


def test_same_weight_units():
    assert convert('100', 'g', 'g') == 100


def test_c_to_k():
    assert convert('25', 'c', 'k') == 298.15


def test_k_to_c():
    assert convert('300', 'k', 'c') == pytest.approx(26.85)


def test_c_to_f():
    assert convert('100', 'c', 'f') == 212


def test_f_to_c():
    assert convert('32', 'f', 'c') == 0


def test_k_to_f():
    assert convert('273.15', 'k', 'f') == 32


def test_f_to_k():
    assert convert('212', 'f', 'k') == 373.15


def test_unique_c_to_f():
    assert convert('-40', 'c', 'f') == -40


def test_abs_zero():
    assert convert('0', 'k', 'c') == -273.15


def test_same_temperature_units():
    assert convert('25', 'c', 'c') == 25


def test_uppercase_units():
    assert convert('2500', 'MM', 'KM') == 0.0025


# отрицательные тесты
def test_negative_length():
    with pytest.raises(ValueError):
        convert('-5', 'm', 'cm')


def test_negative_weight():
    with pytest.raises(ValueError):
        convert('-3', 'kg', 'g')


def test_temperature_below_abs_zero_c_to_k():
    with pytest.raises(ValueError):
        convert('-350', 'c', 'k')


def test_temperature_below_abs_zero_k_to_c():
    with pytest.raises(ValueError):
        convert('-1', 'k', 'c')


def test_temperature_below_abs_zero_f_to_c():
    with pytest.raises(ValueError):
        convert('-500', 'f', 'c')


def test_same_temperature_units_with_abs_zero():
    with pytest.raises(ValueError):
        convert('-1', 'k', 'k')


def test_incompatible_units():
    with pytest.raises(ValueError):
        convert('1', 'kg', 'cm')


def test_invalid_number():
    with pytest.raises(ValueError):
        convert('100a', 'g', 'kg')


def test_invalid_units():
    with pytest.raises(ValueError):
        convert('10', 'abc', 'm')


def test_empty_value():
    with pytest.raises(ValueError):
        convert('', 'mm', 'm')


def test_empty_units():
    with pytest.raises(ValueError):
        convert('100', 'm', '')