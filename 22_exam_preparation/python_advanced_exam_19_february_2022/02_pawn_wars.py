from collections import deque


def square(pos):
    return f'{chr(97 + pos[1])}{8 - pos[0]}'


board = []
w_pos = []
b_pos = []

for row in range(8):
    board.append(input().split())

    if 'w' in board[row]:
        w_pos = [row, board[row].index('w')]

    if 'b' in board[row]:
        b_pos = [row, board[row].index('b')]

positions = {
    "White": w_pos,
    "Black": b_pos
}
movement = {
    "White": -1,
    "Black": 1
}
name = {
    "White": 'w',
    "Black": 'b'
}
turn = deque(["White", "Black"])

while True:
    player = turn[0]
    move = movement[player]
    win_position = []

    if 0 <= (positions[player][0] + move) < 8 and 0 <= (positions[player][1] + move) < 8:
        if board[positions[player][0] + move][positions[player][1] + move] != "-":
            win_position = [positions[player][0] + move, positions[player][1] + move]

    if 0 <= (positions[player][0] + move) < 8 and 0 <= (positions[player][1] - move) < 8:
        if board[positions[player][0] + move][positions[player][1] - move] != "-":
            win_position = [positions[player][0] + move, positions[player][1] - move]

    if win_position:
        print(f"Game over! {player} win, capture on {square(win_position)}.")
        break
    board[positions[player][0]][positions[player][1]] = '-'
    positions[player][0] += move
    board[positions[player][0]][positions[player][1]] = name[player]

    if positions["White"][0] == 0 or positions["Black"][0] == 7:
        print(f"Game over! {player} pawn is promoted to a queen at {square(positions[player])}.")
        break

    turn.reverse()
