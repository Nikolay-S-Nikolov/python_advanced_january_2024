from collections import deque

rows, cols = list(map(int, input().split()))

snake = list(input())
snake_copy = deque(snake)

for row in range(rows):
    while len(snake_copy) < cols:
        snake_copy.extend(snake)
    if row % 2 == 0:
        print(*[snake_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[snake_copy.popleft() for _ in range(cols)][::-1], sep='')
