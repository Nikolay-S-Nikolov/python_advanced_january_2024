SIZE = 5

count_targets = 0
field = []
my_position = []

for row in range(SIZE):
    field.append(input().split())
    count_targets += field[row].count("x")
    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]

commands_count = int(input())
directions = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0),
}

targets_position = []
shot_targets = 0

for _ in range(commands_count):
    action, *info = input().split()
    if action == 'move':
        direction, steps = info[0], int(info[1])
        new_pos_row = my_position[0] + directions[direction][0] * steps
        new_pos_col = my_position[1] + directions[direction][1] * steps
        if {new_pos_row, new_pos_col}.issubset(range(SIZE)):
            if field[new_pos_row][new_pos_col] != 'x':
                my_position = [new_pos_row, new_pos_col]

    elif action == 'shoot':
        direction = info[0]
        new_pos_row = my_position[0] + directions[direction][0]
        new_pos_col = my_position[1] + directions[direction][1]
        while True:

            if {new_pos_row, new_pos_col}.issubset(range(SIZE)):
                if field[new_pos_row][new_pos_col] == 'x':
                    targets_position.append([new_pos_row, new_pos_col])
                    shot_targets += 1
                    field[new_pos_row][new_pos_col] = '.'
                    break
            else:
                break
            new_pos_row += directions[direction][0]
            new_pos_col += directions[direction][1]
    if count_targets == shot_targets:
        break
if count_targets == shot_targets:
    print(f"Training completed! All {count_targets} targets hit.")
    [print(target) for target in targets_position]
else:
    count_left_targets = count_targets - shot_targets
    print(f"Training not completed! {count_left_targets} targets left.")
    if targets_position:
        [print(target) for target in targets_position]
