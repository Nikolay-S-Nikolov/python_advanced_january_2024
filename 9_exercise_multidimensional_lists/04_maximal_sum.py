rows, cols = [int(x) for x in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]
max_sum = float('-inf')
max_matrix = []
for i in range(rows - 2):
    for j in range(cols - 2):
        first_row = matrix[i][j:j + 3]
        second_row = matrix[i + 1][j:j + 3]
        third_row = matrix[i + 2][j:j + 3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        # current_sum = sum([matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]) \
        #               + sum([matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]) \
        #               + sum([matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]])
        if current_sum > max_sum:
            max_matrix = [first_row, second_row, third_row]
            # max_matrix = [
            #     [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
            #     [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
            #     [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
            # ]
            max_sum = current_sum

print(f"Sum = {max_sum}")
[print(*element) for element in max_matrix]
# for elements in max_matrix:
#     print(' '.join([str(x) for x in elements]))
