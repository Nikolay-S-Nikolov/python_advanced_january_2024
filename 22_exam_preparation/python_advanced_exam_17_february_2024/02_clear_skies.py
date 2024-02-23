ARMOR = 300

n = int(input())

airspace = []
jetfighter_pos = []
enemy_count = 4

for row in range(n):
    airspace.append(list(input()))

    if "J" in airspace[row]:
        jetfighter_pos.append(row)
        jetfighter_pos.append(airspace[row].index('J'))

move_command = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}
airspace[jetfighter_pos[0]][jetfighter_pos[1]] = "-"
while ARMOR:
    command = input()
    r, c = move_command[command](jetfighter_pos)
    symbol = airspace[r][c]
    airspace[r][c] = '-'
    jetfighter_pos = [r, c]

    if symbol == 'E':
        if enemy_count > 1:
            enemy_count -= 1
            ARMOR -= 100
        else:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

    elif symbol == 'R':
        ARMOR = 300

if not ARMOR:
    print(
        f"Mission failed, your jetfighter was shot down! Last coordinates [{jetfighter_pos[0]}, {jetfighter_pos[1]}]!")

airspace[jetfighter_pos[0]][jetfighter_pos[1]] = "J"

[print(''.join(airspace_row)) for airspace_row in airspace]
