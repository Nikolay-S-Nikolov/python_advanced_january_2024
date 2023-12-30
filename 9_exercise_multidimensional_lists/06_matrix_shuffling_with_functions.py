def valid_indices(list_idx):
    return {list_idx[0], list_idx[2]}.issubset(valid_row) \
           and {list_idx[1], list_idx[3]}.issubset(valid_col)


def swap_command(swap, indices):
    if valid_indices(indices) and swap == 'swap' and len(indices) == 4:
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(' '.join(r)) for r in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
valid_row = range(rows)
valid_col = range(cols)

matrix = [input().split() for _ in range(rows)]

command = input()

while command != 'END':

    action, *info = [int(x) if x.isdigit() else x for x in command.split()]
    swap_command(action, info)

    command = input()
