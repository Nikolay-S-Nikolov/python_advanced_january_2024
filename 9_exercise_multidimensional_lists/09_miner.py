from collections import deque


def valid_index(r, c):
    if {r, c}.issubset(range(field_size)):
        validated = True
    else:
        validated = False
    return validated


def move_index(direction, current_row, current_col):
    new_row = ''
    new_col = ''
    if direction == "left":
        new_row = current_row
        new_col = current_col - 1
    elif direction == "right":
        new_row = current_row
        new_col = current_col + 1
    elif direction == "up":
        new_row = current_row - 1
        new_col = current_col
    elif direction == "down":
        new_row = current_row + 1
        new_col = current_col
    if valid_index(new_row, new_col):
        return new_row, new_col
    else:
        return current_row, current_col


def miner_move(matrix, command, row, col, coals, end):
    move_direction = command.popleft()
    next_row, next_col = move_index(move_direction, row, col)
    if matrix[next_row][next_col] == 'c':
        coals -= 1
        matrix[next_row][next_col] = '*'
    elif matrix[next_row][next_col] == 'e':
        end = True

    return matrix, command, next_row, next_col, coals, end


field_size = int(input())
move_commands = deque(input().split())
field_matrix = [input().split() for _ in range(field_size)]
miner_row = [i for i in range(field_size) if "s" in field_matrix[i]][0]
miner_col = [j for j in range(field_size) if field_matrix[miner_row][j] == "s"][0]
total_coals = sum(1 for i in range(field_size) for j in range(field_size) if field_matrix[i][j] == 'c')

e_position = False
while move_commands:
    field_matrix, move_commands, miner_row, miner_col, total_coals, e_position \
        = miner_move(field_matrix, move_commands, miner_row, miner_col, total_coals, e_position)
    if e_position:
        print(f"Game over! ({miner_row}, {miner_col})")
        break
    if total_coals == 0:  # it is not defined if total_coals can be 0 in the start.
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        break

if not move_commands and total_coals != 0 and not e_position:
    print(f"{total_coals} pieces of coal left. ({miner_row}, {miner_col})")
