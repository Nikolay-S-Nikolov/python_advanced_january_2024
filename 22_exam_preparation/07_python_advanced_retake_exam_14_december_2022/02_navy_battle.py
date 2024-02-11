n = int(input())

battlefield = []
submarine_pos = []

for row in range(n):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        submarine_pos.append(row)
        submarine_pos.append(battlefield[row].index("S"))

move_functions = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}

mine_damage = 0
destroyed_cruisers = 0

while mine_damage != 3:

    if destroyed_cruisers == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    battlefield[submarine_pos[0]][submarine_pos[1]] = '-'
    r, c = move_functions[input()](submarine_pos)

    if battlefield[r][c] == '*':
        mine_damage += 1

    elif battlefield[r][c] == 'C':
        destroyed_cruisers += 1

    battlefield[r][c] = 'S'
    submarine_pos = [r, c]

else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")

[print(''.join(field_row)) for field_row in battlefield]
