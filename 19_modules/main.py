from triangle.drawing import draw_num_triangle
from math_operations.math_operations import math_operations
from fibonacci.fibonacci_sequence import create_sequence, locate_num

# num = int(input())
# draw_num_triangle(num)
#
# number_one, symbol, number_two = input().split()
# print(f"{math_operations(float(number_one), symbol, float(number_two)):.2f}")

command = input()
fibonacci_seq = []

while command != "Stop":
    command = command.split()

    if command[0] == 'Create':
        fibonacci_seq = create_sequence(int(command[-1]))
        print(*fibonacci_seq)

    elif command[0] == 'Locate':
        locate_num(int(command[-1]), fibonacci_seq)

    command = input()
