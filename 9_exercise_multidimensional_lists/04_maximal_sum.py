rows, cols = [int(x) for x in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]
max_sum = float('-inf')
max_matrix = []
for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = sum([matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]) \
                      + sum([matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]) \
                      + sum([matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]])
        if current_sum > max_sum:
            max_matrix = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
            ]
            max_sum = current_sum

print(f"Sum = {max_sum}")
for elements in max_matrix:
    print(' '.join([str(x) for x in elements]))
