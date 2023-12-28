# Variant 1

# rows = int(input())
# matrix = []
# # for row in range(rows):
# #     matrix.append([int(x) for x in input().split(', ')])
# #
# # flattened = []
# # for row in matrix:
# #     for el in row:
# #         flattened.append(el)
# print(flattened)

#  Variant 2

# rows = int(input())
# matrix = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])
#
# flattened = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         flattened.append(matrix[row][col])
# print(flattened)

# Variant 3

rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
# matrix = []
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])

flattened = [el for row in matrix for el in row]
# for row in matrix:
#     for el in row:
#         flattened.append(el)

print(flattened)

