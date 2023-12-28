rows, cols = [int(x) for x in input().split(', ')]
matrix = []
numbers_sum = 0
for idx in range(rows):
    element = [int(x) for x in input().split(', ')]
    matrix.append(element)
    numbers_sum += sum(element)

print(numbers_sum)
print(matrix)
