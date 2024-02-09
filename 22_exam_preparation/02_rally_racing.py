n = int(input())
racing_number = input()

car_pos = [0, 0]
race_route = []
distance_covered = 0
tunnels_pos = []

for row in range(n):
    race_route.append(input().split(' '))

    if 'T' in race_route[row]:
        tunnels_pos.append([row, race_route[row].index('T')])

command_move = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}
command = input()
while command != 'End':

    r, c = command_move[command](car_pos)
    car_pos = [r, c]
    distance_covered += 10

    if race_route[r][c] == 'F':
        print(f"Racing car {racing_number} finished the stage!")
        break

    if race_route[r][c] == 'T':

        for x, y in tunnels_pos:
            race_route[x][y] = '.'

        tunnels_pos.remove([r, c])
        car_pos = tunnels_pos[0]
        distance_covered += 20

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {distance_covered} km.")

race_route[car_pos[0]][car_pos[1]] = 'C'
[print(''.join(race_root_row)) for race_root_row in race_route]
