def print_board(board):
    [print(''.join(board[board_row])) for board_row in range(size)]


def position_check(mark, money):

    if mark == 'J':
        money += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
        game_board[r][c] = 'G'
        print_board(game_board)
        raise SystemExit

    elif mark == 'W':
        money += 100

    elif mark == 'P':
        money -= 200

    return money


size = int(input())

player_pos = []
game_board = []
amount = 100

for row in range(size):
    game_board.append(list(input()))

    if 'G' in game_board[row]:
        player_pos.append(row)
        player_pos.append(game_board[row].index("G"))

player_move = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1)
}

game_over = False
command = input()

while command != 'end':

    game_board[player_pos[0]][player_pos[1]] = '-'
    r, c = player_move[command](player_pos)

    try:
        position_mark = game_board[r][c]

    except IndexError:
        game_over = True
        break

    amount = position_check(position_mark, amount)

    if amount <= 0:
        game_over = True
        break

    game_board[r][c] = 'G'
    player_pos = [r, c]
    command = input()

if game_over:
    print(f"Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {amount}$")
    print_board(game_board)