rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])


for j in range(cols):
    sum_col_num = 0
    for i in range(rows):
        sum_col_num += matrix[i][j]
    print(sum_col_num)
