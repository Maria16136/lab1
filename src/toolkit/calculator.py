from .tokenizer import string_tokenization
from .validator import validation

from src.constants import digits
from src.constants import operation_symbols


def operation_priority(sign):
    if sign in operation_symbols[:2]:
        return 1
    else:
        return 2


def postfix_entry(tokens):
    result = []
    operations = []
    for token in tokens:
        if token[-1] in digits:
            result.append(token)
        elif not operations:
            operations.append(token)
        elif operation_priority(token) > operation_priority(operations[-1]):
            operations.append(token)
        else:
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
            if str(math_exp[i]) in operation_symbols:
                math_exp[i] = binary_operation(math_exp[i - 2], math_exp[i], math_exp[i - 1])
                del math_exp[i - 1]
                del math_exp[i - 2]
                i -= 1
            else:
                i += 1
        return math_exp
    else:
        raise ValueError('Введено некорректное выражение')