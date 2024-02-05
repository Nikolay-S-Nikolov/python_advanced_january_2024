n, m = [int(x) for x in input().split(',')]

area = []
mouse_pos = []
cheese_count = 0

for row in range(n):
    area.append(list(input()))
    cheese_count += area[row].count('C')

    if "M" in area[row]:
        mouse_pos.append(row)
        mouse_pos.append(area[row].index('M'))

move_direction = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),

}
area[mouse_pos[0]][mouse_pos[1]] = '*'

while True:
    direction = input()

    if direction == 'danger':
        print("Mouse will come back later!")
        break

    r, c = move_direction[direction](mouse_pos)

    if not (0 <= r < n and 0 <= c < m):
        print("No more cheese for tonight!")
        break

    if area[r][c] == '@':
        continue

    mouse_pos = [r, c]

    if area[r][c] == 'C':
        area[r][c] = "*"
        cheese_count -= 1

        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif area[r][c] == 'T':
        print("Mouse is trapped!")
        break

area[mouse_pos[0]][mouse_pos[1]] = 'M'

[print(''.join(area_row)) for area_row in area]
