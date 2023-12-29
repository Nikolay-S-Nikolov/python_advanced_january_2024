rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_diagonal = [matrix[x][x] for x in range(rows)]
secondary_diagonal = [matrix[x][-x - 1] for x in range(rows)]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)

