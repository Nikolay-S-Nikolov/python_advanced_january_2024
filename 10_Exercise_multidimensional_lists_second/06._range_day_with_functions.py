def command_move(direction: str, steps: int):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == 'x':
        return my_position
    return [r, c]


def shot(direction: str):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]
    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5

count_targets = 0
field = []
my_position = []

for row in range(SIZE):
    field.append(input().split())
    count_targets += field[row].count("x")
    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

targets_position = []
hit_targets = 0

for _ in range(int(input())):
    action, *info = input().split()
    if action == 'move':
        my_position = command_move(info[0], int(info[1]))

    elif action == 'shoot':
        target_position = shot(info[0])
        if target_position:
            targets_position.append(target_position)
            hit_targets += 1
        if hit_targets == count_targets:
            print(f"Training completed! All {count_targets} targets hit.")
            break
else:
    print(f"Training not completed! {count_targets - hit_targets} targets left.")

print(*targets_position, sep='\n')