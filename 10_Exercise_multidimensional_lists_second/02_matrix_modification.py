n_rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n_rows)]

command = input()
while command != 'END':
    action, row, col, value = command.split()[0], int(command.split()[1]), int(command.split()[2]), \
                              int(command.split()[3])
    if {row, col}.issubset(range(n_rows)):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

[print(*ele) for ele in matrix]
