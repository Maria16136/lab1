from src.constants import digits
from src.constants import unary_operators
from src.constants import operation_symbols


def corr_numb(token):
    if token == '+0' or token == '-0':
        token = '0'
    if not token:
        return False
    if len(token) == 1:
        return token in digits
    if len(token) > 1:
        if token.count('.') > 1:
            return False
        elif token.count('.') == 1:
            if len(token) < 3:
                return False
            if token[0] in unary_operators:
                token = token[1:]
            whole_part = token.split('.')[0]
            fractional_part = token.split('.')[1]
            if len(whole_part) == 1:
                return all(symb in digits for symb in fractional_part) and whole_part in digits
            return all(symb in digits for symb in fractional_part) and whole_part[0] != '0' \
                and all(symb in digits for symb in fractional_part[1:])
        else:
            return (all(symb in digits for symb in token[1:]) and token[0] in unary_operators and token[1] != '0') \
                or (all(symb in digits for symb in token) and token[0] != '0')


def corr_sign(token):
    return len(token) == 1 and token in operation_symbols


def validation(tokens):
    if len(tokens) == 0 or not corr_numb(tokens[0]) or not corr_numb(tokens[-1]):
        return False
    else:
        for i in range(len(tokens) - 1):
            if tokens[i] == '/' and corr_numb(tokens[i + 1]) and float(tokens[i + 1]) == 0:
                return False
            if (corr_numb(tokens[i]) and corr_sign(tokens[i + 1])) or \
                    (corr_numb(tokens[i + 1]) and corr_sign(tokens[i])):
                continue
            else:
                return False
    return True