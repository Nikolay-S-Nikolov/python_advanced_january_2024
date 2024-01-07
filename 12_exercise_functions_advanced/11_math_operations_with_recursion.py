def math_operations(*float_values, **operations):
    length = 4 if len(float_values) > 4 else len(float_values)

    for index in range(length):
        if index == 0:
            operations["a"] += float_values[index]

        elif index == 1:
            operations["s"] -= float_values[index]

        elif index == 2:
            if float_values[index] != 0:
                operations["d"] /= float_values[index]

        elif index == 3:
            operations["m"] *= float_values[index]

    float_values = float_values[length:]

    if not float_values:
        return '\n'.join([f"{k}: {v:.1f}" for k, v in sorted(operations.items(), key=lambda x: (-x[1], x[0]))])

    return math_operations(*float_values, **operations)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print("\n----------------- \n")

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print("\n----------------- \n")

print(math_operations(6.0, a=0, s=0, d=5, m=0))
