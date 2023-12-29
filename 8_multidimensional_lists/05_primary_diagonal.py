int_n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(int_n)]

# for i_j in range(int_n):
# #     sum_primary_diagonal += matrix[i_j][i_j]
# print(sum_primary_diagonal)
print(sum([matrix[i_j][i_j] for i_j in range(int_n)]))
