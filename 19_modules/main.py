from triangle.drawing import draw_num_triangle
from math_operations.math_operations import math_operations

num = int(input())
draw_num_triangle(num)

number_one, symbol, number_two = input().split()
print(f"{math_operations(float(number_one), symbol, float(number_two)):.2f}")
