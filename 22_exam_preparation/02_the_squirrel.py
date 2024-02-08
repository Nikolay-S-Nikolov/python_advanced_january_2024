from collections import deque

size = int(input())
commands = deque(input().split(', '))

squirrel_pos = []
field = []

for row in range(size):
    field.append(list(input()))

    if "s" in field[row]:
        squirrel_pos.append(row)
        squirrel_pos.append(field[row].index('s'))

move_functions = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}

collected_hazelnuts = 0

for direction in commands:
    r, c = move_functions[direction](squirrel_pos)

    if not (0 <= r < size and 0 <= c < size):
        print("The squirrel is out of the field.")
        break

    if field[r][c] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if field[r][c] == 'h':
        collected_hazelnuts += 1
        field[r][c] = '*'

        if collected_hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    squirrel_pos = [r, c]

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
