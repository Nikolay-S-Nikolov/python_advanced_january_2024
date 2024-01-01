num = int(input())

eggs_matrix = [[x for x in input().split()] for _ in range(num)]

bunny_row = [r for r in range(num) if "B" in eggs_matrix[r]][0]
bunny_col = [c for c in range(num) if eggs_matrix[bunny_row][c] == 'B'][0]
# bunny_col = eggs_matrix[bunny_row].index('B')

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

max_num_eggs = 0
best_path = []
best_direction = None

for direction, pos in moves.items():
    row, col = [pos[0] + bunny_row, pos[1] + bunny_col]
    current_eggs_num = 0
    current_path = []
    while {row, col}.issubset(range(num)):
        if eggs_matrix[row][col] == 'X':
            break
        current_eggs_num += int(eggs_matrix[row][col])
        current_path.append([row, col])
        row += pos[0]
        col += pos[1]

    if current_eggs_num >= max_num_eggs:
        max_num_eggs = current_eggs_num
        best_path = current_path
        best_direction = direction

print(best_direction)
[print(ele) for ele in best_path]
print(max_num_eggs)
