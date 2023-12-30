from collections import deque


def detonate(matrix_bombs, indexes):
    row, col = [int(x) for x in indexes.popleft().split(',')]
    if matrix_bombs[row][col] <= 0:
        return matrix_bombs, indexes
    explosion_value = matrix_bombs[row][col]
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if {r, c}.issubset(range(n)) and matrix_bombs[r][c] > 0:
                matrix_bombs[r][c] -= explosion_value
    return matrix_bombs, indexes


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = deque(input().split())

while coordinates:
    matrix, coordinates = detonate(matrix, coordinates)

alive_cells = [x for row in matrix for x in row if x > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]


