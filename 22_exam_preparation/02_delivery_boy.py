row, col = [int(x) for x in input().split()]

field = []
boy_pos = []

for idx in range(row):
    field.append(list(input()))

    if 'B' in field[idx]:
        boy_pos.append(idx)
        boy_pos.append(field[idx].index('B'))

start_r, start_c = boy_pos

move_functions = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}

while True:
    r, c = move_functions[input()](boy_pos)

    if not (0 <= r < row and 0 <= c < col):
        print("The delivery is late. Order is canceled.")
        field[start_r][start_c] = ' '
        break

    if field[r][c] == 'A':
        print("Pizza is delivered on time! Next order...")
        field[r][c] = 'P'
        break

    if field[r][c] == '*':
        continue

    elif field[r][c] == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        field[r][c] = 'R'

    elif field[r][c] == '-':
        field[r][c] = '.'

    boy_pos = [r, c]

[print(''.join(row_field)) for row_field in field]
