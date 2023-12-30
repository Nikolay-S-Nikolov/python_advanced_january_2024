rows, cols = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    matrix.append([])
    first_last_letter = chr(ord('a') + row)
    for col in range(cols):
        middle_letter = chr(ord(first_last_letter) + col)
        matrix[row].append(first_last_letter + middle_letter + first_last_letter)

[print(" ".join(element)) for element in matrix]
