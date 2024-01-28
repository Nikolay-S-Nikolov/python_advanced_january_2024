from collections import deque


def symbol_position_check(matrix, r, c, player_sym):
    if 0 <= r < ROW and 0 <= c < COL:
        if matrix[r][c] != player_sym:
            return True
    elif not (0 <= r < ROW and 0 <= c < COL):
        return True
    return False


def player_win(matrix, symbol, row, col, draw_counter):
    if draw_counter == COL * ROW:
        print(f'Draw game!')
        print_board(board)
        raise SystemExit

    for x, y in mapper:
        counter = 1
        for i in range(1, 4):
            check_row = row + x * i
            check_col = col + y * i
            if symbol_position_check(matrix, check_row, check_col, symbol):
                break
            counter += 1
        for i in range(1, 4):
            check_row = row - x * i
            check_col = col - y * i
            if symbol_position_check(matrix, check_row, check_col, symbol):
                break
            counter += 1
        if counter >= 4:
            return True
    return False


def row_to_place_symbol(matrix, column):
    row = ROW - 1
    while row != -1 and matrix[row][column] != 0:
        row -= 1
    return row


def not_valid_column(column_number):
    if 0 <= column_number <= COL:
        return False
    return True


def print_board(matrix):
    return [print(f'{row}') for row in matrix]


COL, ROW = 7, 6

board = [[0] * COL for _ in range(ROW)]
player_one_symbol, player_two_symbol = input('Please choose a symbol for player 1: '), input(
    'Please choose a symbol for player 2: ')
turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
mapper = [
    (-1, 0),  # Down
    (0, -1),  # Left
    (1, 1),  # Diagonal Down Right
    (1, -1),  # Diagonal Down Left
]
win = False
even_score_counter = 0

while True:
    print_board(board)
    player_number, player_symbol = turn[0]

    try:
        player_col = int(input(f"Player {player_number}, please choose a column: ")) - 1
        if not_valid_column(player_col):
            raise ValueError
    except ValueError:
        print(f'Select a valid number in the range (1-{COL})')
        continue
    available_row = row_to_place_symbol(board, player_col)
    if board[available_row][player_col] == 0:
        board[available_row][player_col] = player_symbol
    else:
        print(f'No empty space in chosen column')
        continue
    even_score_counter += 1
    if player_win(board, player_symbol, available_row, player_col, even_score_counter):
        print(f'Player{player_number} win!')
        print_board(board)
        break
    turn.rotate()
