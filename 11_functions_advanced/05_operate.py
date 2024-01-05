from functools import reduce


def operate(operator, *args):
    result = reduce(lambda a, b: eval(f'{a}{operator}{b}'), args)
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))