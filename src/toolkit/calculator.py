from src.constants import DIGITS, OPERATION_SYMBOLS

from .tokenizer import string_tokenization
from .validator import validation


def operation_priority(sign):
    if sign in OPERATION_SYMBOLS[:2]:
        return 1
    else:
        return 2


def postfix_entry(tokens):
    result = []
    operations = []
    for token in tokens:
        if token[-1] in DIGITS:
            result.append(token)
        elif not operations or operation_priority(token) > operation_priority(operations[-1]):
            operations.append(token)
        else:
            while operations and operation_priority(token) <= operation_priority(operations[-1]):
                result.append(operations[-1])
                del operations[-1]
            operations.append(token)
    return result + operations[::-1]


def binary_operation(number_1, operation, number_2):
    if operation == '+':
        return float(number_1) + float(number_2)
    if operation == '-':
        return float(number_1) - float(number_2)
    if operation == '*':
        return float(number_1) * float(number_2)
    if operation == '/':
        return float(number_1) / float(number_2)


def calc(math_expression):
    tokens = string_tokenization(math_expression)
    verified_tokens = validation(tokens)
    if verified_tokens:
        math_exp = postfix_entry(tokens)
        i = 0
        while len(math_exp) > 1:
            if str(math_exp[i]) in OPERATION_SYMBOLS:
                math_exp[i] = binary_operation(math_exp[i - 2], math_exp[i], math_exp[i - 1])
                del math_exp[i - 1]
                del math_exp[i - 2]
                i -= 1
            else:
                i += 1
        return float(math_exp[0])
    else:
        raise ValueError('Введено некорректное выражение')