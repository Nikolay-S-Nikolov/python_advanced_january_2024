stars = 2

size = int(input())
field = []
player_pos = []

for row in range(size):
    field.append(input().split())

    if 'P' in field[row]:
        player_pos.append(row)
        player_pos.append(field[row].index('P'))

move_dict = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}

field[player_pos[0]][player_pos[1]] = '.'

while stars != 10 and stars != 0:

    r, c = move_dict[input()](player_pos)
    if not 0 <= r < size or not 0 <= c < size:
        r, c = 0, 0

    symbol = field[r][c]

    if symbol == "*":
        field[r][c] = '.'
        stars += 1

    elif symbol == "#":
        stars -= 1
        continue

    player_pos = [r, c]

if not stars:
    print("Game over! You are out of any stars.")
else:
    print("You won! You have collected 10 stars.")

field[player_pos[0]][player_pos[1]] = 'P'

print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")

[print(f"{' '.join(row)}") for row in field]
