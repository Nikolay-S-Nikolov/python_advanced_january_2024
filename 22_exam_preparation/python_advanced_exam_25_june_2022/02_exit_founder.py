from collections import deque

players = deque(input().split(', '))
maze_board = [input().split() for _ in range(6)]

hits_a_wall = {
    'Tom': False,
    'Jerry': False
}

while True:

    player = players[0]
    r, c = [int(x) for x in list(input()) if x.isdigit()]

    if hits_a_wall[player]:
        hits_a_wall[player] = False

    elif maze_board[r][c] == "W":
        print(f"{player} hits a wall and needs to rest.")
        hits_a_wall[player] = True

    elif maze_board[r][c] == "E":
        print(f"{player} found the Exit and wins the game!")
        break

    elif maze_board[r][c] == "T":
        print(f"{player} is out of the game! The winner is {players[1]}.")
        break

    players.rotate()
