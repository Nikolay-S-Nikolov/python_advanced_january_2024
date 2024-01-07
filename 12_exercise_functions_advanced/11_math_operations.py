def math_operations(*float_values, **operations):
    for i in range(len(float_values)):
        key = list(operations.keys())[i % 4]
        if key == "a":
            operations[key] += float_values[i]
        elif key == 's':
            operations[key] -= float_values[i]
        elif key == 'd':
            if float_values[i] != 0:
                operations[key] /= float_values[i]
        elif key == 'm':
            operations[key] *= float_values[i]
    return '\n'.join([f"{k}: {v:.1f}" for k, v in sorted(operations.items(), key=lambda x: (-x[1], x[0]))])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print("\n----------------- \n")

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print("\n----------------- \n")

print(math_operations(6.0, a=0, s=0, d=5, m=0))
