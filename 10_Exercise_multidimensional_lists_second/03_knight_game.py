size_n = int(input())
knights_matrix = [list(input()) for _ in range(size_n)]

knights_removed = 0

moves = (
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
)

while True:
    greatest_number_attacks = 0
    pos_knight_to_remove = []
    for row in range(size_n):
        for col in range(size_n):
            if knights_matrix[row][col] == 'K':
                attacks = 0
                for r, c in moves:
                    new_row, new_col = row + r, col + c
                    if {new_row, new_col}.issubset(range(size_n)) and knights_matrix[new_row][new_col] == 'K':
                        attacks += 1
                if attacks > greatest_number_attacks:
                    pos_knight_to_remove = [row, col]
                    greatest_number_attacks = attacks
    if pos_knight_to_remove:
        knights_matrix[pos_knight_to_remove[0]][pos_knight_to_remove[1]] = '0'
        knights_removed += 1
    else:
        break

print(knights_removed)
