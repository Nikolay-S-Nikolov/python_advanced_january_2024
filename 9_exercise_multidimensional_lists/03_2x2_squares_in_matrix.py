rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
counter = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        first = matrix[row][col]
        second = matrix[row][col + 1]
        third = matrix[row + 1][col]
        forth = matrix[row + 1][col + 1]
        if first == second and second == third and third == forth:
            counter += 1
print(counter)
