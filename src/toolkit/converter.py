from src.constants import (
    ABS_ZERO_FAHRENHEIT,
    ABS_ZERO_KELVIN,
    C_TO_F_SCALE,
    FAHRENHEIT_OFFSET,
    G_TO_KG_SCALE,
    KELVIN_OFFSET,
    LENGTH,
    TEMPERATURE,
    WEIGHT,
)

from .validator import corr_numb


def convert(value: str, unit_from: str, unit_to: str) -> float:
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    result = ''
    if unit_from in LENGTH and unit_to in LENGTH and corr_numb(value) and float(value) >= 0:
        if LENGTH.index(unit_from) > LENGTH.index(unit_to):
            result = float(value) * 10 ** sum(range(LENGTH.index(unit_to) + 1, LENGTH.index(unit_from) + 1))
        elif LENGTH.index(unit_from) == LENGTH.index(unit_to):
            result = float(value)
        else:
            result = float(value) / 10 ** sum(range(LENGTH.index(unit_from) + 1, LENGTH.index(unit_to) + 1))
    elif unit_from in WEIGHT and unit_to in WEIGHT and corr_numb(value) and float(value) >= 0:
        if WEIGHT.index(unit_from) > WEIGHT.index(unit_to):
            result = float(value) * G_TO_KG_SCALE
        elif WEIGHT.index(unit_from) == WEIGHT.index(unit_to):
            result = float(value)
        else:
            result = float(value) / G_TO_KG_SCALE
    elif unit_from in TEMPERATURE and unit_to in TEMPERATURE and corr_numb(value):
        if TEMPERATURE.index(unit_from) == TEMPERATURE.index(unit_to) and \
                ((unit_from == TEMPERATURE[0] and float(value) >= -KELVIN_OFFSET) or
                 (unit_from == TEMPERATURE[1] and float(value) >= ABS_ZERO_KELVIN) or
                 (unit_from == TEMPERATURE[2] and float(value) >= ABS_ZERO_FAHRENHEIT)):
            result = float(value)
        elif TEMPERATURE.index(unit_from) == 0 and TEMPERATURE.index(unit_to) == 1:
            possible_result = float(value) + KELVIN_OFFSET
            if possible_result >= ABS_ZERO_KELVIN:
                result = possible_result
        elif TEMPERATURE.index(unit_from) == 1 and TEMPERATURE.index(unit_to) == 0:
            possible_result = float(value) - KELVIN_OFFSET
            if possible_result >= -KELVIN_OFFSET:
                result = possible_result
        elif TEMPERATURE.index(unit_from) == 0 and TEMPERATURE.index(unit_to) == 2:
            possible_result = float(value) * C_TO_F_SCALE + FAHRENHEIT_OFFSET
            if possible_result >= ABS_ZERO_FAHRENHEIT:
                result = possible_result
        elif TEMPERATURE.index(unit_from) == 2 and TEMPERATURE.index(unit_to) == 0:
            possible_result = (float(value) - FAHRENHEIT_OFFSET) / C_TO_F_SCALE
            if possible_result >= -KELVIN_OFFSET:
                result = possible_result
        elif TEMPERATURE.index(unit_from) == 1 and TEMPERATURE.index(unit_to) == 2:
            possible_result = (float(value) - KELVIN_OFFSET) * C_TO_F_SCALE + FAHRENHEIT_OFFSET
            if possible_result >= ABS_ZERO_FAHRENHEIT:
                result = possible_result
        elif TEMPERATURE.index(unit_from) == 2 and TEMPERATURE.index(unit_to) == 1:
            possible_result = (float(value) - FAHRENHEIT_OFFSET) / C_TO_F_SCALE + KELVIN_OFFSET
            if possible_result >= ABS_ZERO_KELVIN:
                result = possible_result
    if result == '':
        raise ValueError('Введено некорректное выражение')
    return result