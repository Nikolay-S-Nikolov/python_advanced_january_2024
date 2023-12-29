i_j = int(input())

matrix = [list(input()) for _ in range(i_j)]

symbol = input()

for row in range(i_j):
    for col in range(i_j):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            raise SystemExit

print(f"{symbol} does not occur in the matrix")


