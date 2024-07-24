HEALTH = 100

n_size = int(input())
maze = []
traveler_pos = []
for row in range(n_size):
    maze.append(list(input()))
    if 'P' in maze[row]:
        traveler_pos.append(row)
        traveler_pos.append(maze[row].index('P'))

move_command = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}
maze[traveler_pos[0]][traveler_pos[1]] = '-'

while HEALTH > 0:
    command = input()
    r, c = move_command[command](traveler_pos)
    if r == n_size or c == n_size:
        continue
    symbol = maze[r][c]
    maze[r][c] = '-'
    traveler_pos = [r, c]

    if symbol == 'M':
        HEALTH -= 40

    elif symbol == 'H':
        HEALTH += 15
        if HEALTH > 100:
            HEALTH = 100

    elif symbol == 'X':
        print('Player escaped the maze. Danger passed!')
        break

if HEALTH <= 0:
    HEALTH = 0
    print('Player is dead. Maze over!')
print(f"Player's health: {HEALTH} units")
maze[traveler_pos[0]][traveler_pos[1]] = 'P'

[print(''.join(maze_row)) for maze_row in maze]
