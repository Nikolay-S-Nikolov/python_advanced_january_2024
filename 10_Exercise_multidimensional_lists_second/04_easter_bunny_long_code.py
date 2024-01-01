num = int(input())

eggs_matrix = [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(num)]

bunny_row = [r for r in range(num) if "B" in eggs_matrix[r]][0]
# bunny_col = [c for c in range(num) if eggs_matrix[bunny_row][c] == 'B'][0]
bunny_col = eggs_matrix[bunny_row].index('B')

moves = ('up', 'down', 'left', 'right')

max_num_eggs = 0
matrix_pos = []
move = ''
for direction in moves:
    current_eggs_num = 0
    positions = []
    if direction == "up":
        for row in range(bunny_row - 1, 0, -1):
            if not eggs_matrix[row][bunny_col] == 'X':
                current_eggs_num += eggs_matrix[row][bunny_col]
                positions.append([row, bunny_col])
            else:
                break

    elif direction == "down":
        for row in range(bunny_row + 1, num):
            if not eggs_matrix[row][bunny_col] == 'X':
                current_eggs_num += eggs_matrix[row][bunny_col]
                positions.append([row, bunny_col])
            else:
                break
    elif direction == "left":
        for col in range(bunny_col - 1, 0, -1):
            if not eggs_matrix[bunny_row][col] == 'X':
                current_eggs_num += eggs_matrix[bunny_row][col]
                positions.append([bunny_row, col])
            else:
                break

    elif direction == "right":
        for col in range(bunny_col + 1, num):
            if not eggs_matrix[bunny_row][col] == 'X':
                current_eggs_num += eggs_matrix[bunny_row][col]
                positions.append([bunny_row, col])
            else:
                break
    if current_eggs_num >= max_num_eggs:
        max_num_eggs = current_eggs_num
        matrix_pos = positions
        move = direction
print(move)
[print(ele) for ele in matrix_pos]
print(max_num_eggs)
