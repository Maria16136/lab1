from src.constants import digits
from src.constants import point
from src.constants import unary_operators
from src.constants import operation_symbols


def corr_numb(token):
    if token == '+0' or token == '-0':
        token = '0'
    if len(token) == 1:
        return token in digits
    if len(token) >= 2:
        if token.count('.') > 1:
            return False
        return (all(symb in digits + point for symb in token[1:]) and token[0] in unary_operators and token[1] != '0') \
                or (all(symb in digits + point for symb in token) and token[0] != '0')


def corr_sign(token):
    return len(token) == 1 and token in operation_symbols


def validation(tokens):
    if len(tokens) == 0 or not corr_numb(tokens[0]) or not corr_numb(tokens[-1]):
        return False
    else:
        for i in range(len(tokens) - 1):
            if tokens[i] == '/' and (tokens[i + 1] == '0' or  tokens[i + 1] == '+0' or tokens[i + 1] == '-0'):
                return False
            if (corr_numb(tokens[i]) and corr_sign(tokens[i + 1])) or \
                    (corr_numb(tokens[i + 1]) and corr_sign(tokens[i])):
                continue
            else:
                return False
    return True