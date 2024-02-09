def create_function(x, y, value):
    if matrix[x][y] == '.':
        matrix[x][y] = value[0]


def update_function(x, y, value):
    if not matrix[x][y] == '.':
        matrix[x][y] = value[0]


def delete_function(x, y, value=None):
    if not matrix[x][y] == '.':
        matrix[x][y] = '.'


def read_function(x, y, value=None):
    if not matrix[x][y] == '.':
        print(matrix[x][y])


matrix = [input().split() for _ in range(6)]
position = [int(x) for x in list(input()) if x.isdigit()]

command = input()

functions = {
    'Create': create_function,
    'Update': update_function,
    'Delete': delete_function,
    'Read': read_function
}

directions = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}

while command != 'Stop':
    action, direction, *data = command.split(', ')
    position = directions[direction](position)
    functions[action](position[0], position[1], data)
    command = input()

[print(' '.join(row)) for row in matrix]
