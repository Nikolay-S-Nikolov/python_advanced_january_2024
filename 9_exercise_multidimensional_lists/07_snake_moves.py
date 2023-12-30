rows, cols = list(map(int, input().split()))
snake_len = rows * cols
snake = input()
word = snake * (snake_len // len(snake) + 1)

for row in range(rows):
    row_word = word[:cols]
    if row % 2 == 0 or row == 0:
        print(row_word)
    else:
        print(row_word[::-1])
    word = word[cols:]
