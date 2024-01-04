presents_num = int(input())
neighborhood_size = int(input())

neighborhood = []
santa_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

count_nice_kids = 0

for rows in range(neighborhood_size):
    neighborhood.append(input().split())

    if 'S' in neighborhood[rows]:
        santa_pos = [rows, neighborhood[rows].index('S')]
    count_nice_kids += neighborhood[rows].count('V')

neighborhood[santa_pos[0]][santa_pos[1]] = '-'

command = input()
delivered_gifts = 0
nice_kids_with_present = 0

while command != 'Christmas morning':
    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
    direction = command
    r = santa_pos[0] + directions[direction][0]
    c = santa_pos[1] + directions[direction][1]

    if neighborhood[r][c] == 'C':

        for direction_around in directions.values():

            if neighborhood[r + direction_around[0]][c + direction_around[1]] == 'X' \
                    or neighborhood[r + direction_around[0]][c + direction_around[1]] == 'V':

                if neighborhood[r + direction_around[0]][c + direction_around[1]] == 'V':
                    nice_kids_with_present += 1

                neighborhood[r + direction_around[0]][c + direction_around[1]] = '-'
                delivered_gifts += 1

                if delivered_gifts == presents_num:
                    break

    else:
        if neighborhood[r][c] == 'V':
            delivered_gifts += 1
            nice_kids_with_present += 1
    santa_pos = [r, c]
    neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

    if delivered_gifts == presents_num:
        break
    command = input()

if count_nice_kids > nice_kids_with_present:
    if delivered_gifts == presents_num:
        print("Santa ran out of presents!")
    [print(' '.join(row)) for row in neighborhood]
    print(f"No presents for {count_nice_kids - nice_kids_with_present} nice kid/s.")
else:
    [print(' '.join(row)) for row in neighborhood]
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
