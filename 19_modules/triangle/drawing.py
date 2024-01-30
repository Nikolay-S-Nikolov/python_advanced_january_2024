def draw_upper_part(n):
    for row in range(1, n + 1):
        [print(num, end=' ') for num in range(1, row + 1)]
        print()


def draw_lower_part(n):
    for row in range(n, 0, -1):
        [print(num, end=' ') for num in range(1, row)]
        print()


def draw_num_triangle(n):
    draw_upper_part(n)
    draw_lower_part(n)
