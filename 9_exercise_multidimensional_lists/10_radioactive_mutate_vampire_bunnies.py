def check_player_alive(row, col):
    if lair_matrix[row][col] == 'B':
        [print(*element, sep='') for element in lair_matrix]
        print(f"dead: {row} {col}")
        raise SystemExit


def show_result(pos_r, pos_c, player='won'):
    bunnies_move(bunnies_position())
    [print(*element, sep='') for element in lair_matrix]
    if player == "dead":
        print(f"dead: {pos_r} {pos_c}")
        raise SystemExit
    else:
        print(f"won: {pos_r} {pos_c}")
        raise SystemExit


def player_movement(row, col, direction):
    new_row, new_col = row + directions[direction][0], col + directions[direction][1]
    if 0 <= new_row < lair_rows and 0 <= new_col < lair_cols:
        if lair_matrix[new_row][new_col] == 'B':
            show_result(new_row, new_col, "dead")
        elif lair_matrix[new_row][new_col] == '.':
            return new_row, new_col
    else:
        show_result(row, col, 'won')


def bunnies_position():
    position = [[i, j] for i in range(lair_rows) for j in range(lair_cols) if lair_matrix[i][j] == 'B']

    return position


def bunnies_move(pos):
    for row, col in pos:
        for bunnie_direction in directions.values():
            new_r, new_c = row + bunnie_direction[0], col + bunnie_direction[1]
            if 0 <= new_r < lair_rows and 0 <= new_c < lair_cols:
                lair_matrix[new_r][new_c] = 'B'


lair_rows, lair_cols = [int(x) for x in input().split()]
lair_matrix = [list(input()) for _ in range(lair_rows)]
commands = input()

player_row = [i for i in range(lair_rows) if "P" in lair_matrix[i]][0]
player_col = [j for j in range(lair_cols) if lair_matrix[player_row][j] == "P"][0]
lair_matrix[player_row][player_col] = '.'

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

for command in commands:
    player_row, player_col = player_movement(player_row, player_col, command)
    bunnies_move(bunnies_position())
    check_player_alive(player_row, player_col)
