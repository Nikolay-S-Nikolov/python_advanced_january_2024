rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    action = command.split()
    if len(action) == 5 and action[0] == 'swap' \
            and int(action[1]) in range(rows) and int(action[3]) in range(rows) \
            and int(action[2]) in range(cols) and int(action[4]) in range(cols):
        row1, col1, row2, col2 = int(action[1]), int(action[2]), int(action[3]), int(action[4])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*el) for el in matrix]

    else:
        print("Invalid input!")
    command = input()
