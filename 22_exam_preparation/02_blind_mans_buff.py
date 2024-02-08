n, m = list(map(int, input().split()))

playground = []
player_pos = []

for row in range(n):
    playground.append(input().split())

    if 'B' in playground[row]:
        player_pos.append(row)
        player_pos.append(playground[row].index('B'))

move_directions = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}

touched_opponents = 0
move_made = 0

while touched_opponents != 3:

    command = input()
    if command == 'Finish':
        break


    r, c = move_directions[command](player_pos)

    if not (0 <= r < n and 0 <= c < m):
        continue

    if playground[r][c] == 'O':
        continue

    move_made += 1

    if playground[r][c] == 'P':
        touched_opponents += 1
        playground[r][c] = '-'

    player_pos = [r, c]

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {move_made}")
