SIZE = 6

board = [input().split() for _ in range(SIZE)]
scored_buckets = []
points = 0

for _ in range(3):
    r, c = [int(x) for x in input().strip("()").split(', ')]
    if not 0 <= r < SIZE or not 0 <= c < SIZE:
        continue

    if board[r][c] == 'B' and not [r, c] in scored_buckets:
        scored_column = [int(board[x][c]) for x in range(SIZE) if board[x][c].isdigit()]
        points += sum(scored_column)
        scored_buckets.append([r, c])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

else:
    prize = ''
    if points < 200:
        prize = 'Football'
    elif points < 300:
        prize = 'Teddy Bear'
    else:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {points} points, and you've won {prize}.")

