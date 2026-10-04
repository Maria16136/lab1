from .validator import corr_numb
from src.constants import (
    length, weight, temperature, g_to_kg_scale, kelvin_offset, c_to_f_scale,
    fahrenheit_offset, abs_zero_fahrenheit, abs_zero_kelvin
)


def convert(value, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    result = ''
    if unit_from in length and unit_to in length and corr_numb(value) and float(value) >= 0:
        if length.index(unit_from) > length.index(unit_to):
            result = float(value) * 10 ** sum(range(length.index(unit_to) + 1, length.index(unit_from) + 1))
        else:
            result = float(value) / 10 ** sum(range(length.index(unit_from) + 1, length.index(unit_to) + 1))
    elif unit_from in weight and unit_to in weight and corr_numb(value) and float(value) >= 0:
        if weight.index(unit_from) > weight.index(unit_to):
            result = float(value) * g_to_kg_scale
        else:
            result = float(value) / g_to_kg_scale
    elif unit_from in temperature and unit_to in temperature and corr_numb(value):
        if temperature.index(unit_from) == 0 and temperature.index(unit_to) == 1:
            possible_result = float(value) + kelvin_offset
            if possible_result >= abs_zero_kelvin:
                result = possible_result
        if temperature.index(unit_from) == 1 and temperature.index(unit_to) == 0:
            possible_result = float(value) - kelvin_offset
            if possible_result >= -kelvin_offset:
                result = possible_result
        if temperature.index(unit_from) == 0 and temperature.index(unit_to) == 2:
            possible_result = float(value) * c_to_f_scale + fahrenheit_offset
            if possible_result >= abs_zero_fahrenheit:
                result = possible_result
        if temperature.index(unit_from) == 2 and temperature.index(unit_to) == 0:
            possible_result = (float(value) - fahrenheit_offset)/ c_to_f_scale
            if possible_result >= -kelvin_offset:
                result = possible_result
        if temperature.index(unit_from) == 1 and temperature.index(unit_to) == 2:
            possible_result = (float(value) - kelvin_offset) * c_to_f_scale + fahrenheit_offset
            if possible_result >= abs_zero_fahrenheit:
                result = possible_result
        if temperature.index(unit_from) == 2 and temperature.index(unit_to) == 1:
            possible_result = (float(value) - fahrenheit_offset) / c_to_f_scale + kelvin_offset
            if possible_result >= abs_zero_kelvin:
                result = possible_result
    if len(str(result)) > 0:
        return result
    else:
        return False