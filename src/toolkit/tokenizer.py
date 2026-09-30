from src.constants import digits
from src.constants import point


def string_tokenization(math_exp):
    math_exp = ''.join(math_exp.split(' '))
    tokens = []
    substring = ''
    for i in range(len(math_exp)):
        if len(substring) == 0:
            substring += math_exp[i]
        elif math_exp[i] in digits or math_exp[i] in point:
            substring += math_exp[i]
        else:
            tokens.append(substring)
            if substring[-1] in digits:
                tokens.append(math_exp[i])
                substring = ''
            else:
                substring = math_exp[i]
        if i + 1 == len(math_exp):
            tokens.append(substring)
    return tokens



