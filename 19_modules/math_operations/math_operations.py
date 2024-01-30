def math_operations(num_1, sign, num_2):
    functions = {
        "/": divide_num,
        "*": multiply_num,
        '-': subtract_num,
        '+': add_num,
        '^': exponentiation_num
    }
    return functions[sign](num_1, num_2)


def divide_num(n_1, n_2):
    return n_1 / n_2


def multiply_num(n_1, n_2):
    return n_1 * n_2


def subtract_num(n_1, n_2):
    return n_1 - n_2


def add_num(n_1, n_2):
    return n_1 + n_2


def exponentiation_num(n_1, n_2):
    return n_1 ** n_2
