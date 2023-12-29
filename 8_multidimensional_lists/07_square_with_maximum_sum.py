rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
max_matrix = []
for row in range(rows - 1):
    for col in range(columns - 1):
        first_num = matrix[row][col]
        below_num = matrix[row + 1][col]
        right_num = matrix[row][col + 1]
        diagonal_num = matrix[row + 1][col + 1]
        current_sum = first_num + below_num + right_num + diagonal_num
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = [[first_num, right_num], [below_num, diagonal_num]]
print(*max_matrix[0])
print(*max_matrix[1])
print(max_sum)
