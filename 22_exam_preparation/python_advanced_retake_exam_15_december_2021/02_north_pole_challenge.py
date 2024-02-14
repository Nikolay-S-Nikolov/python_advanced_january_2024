rows, cols = [int(x) for x in input().split(', ')]

workshop = []
y_pos = []
items = 0

for row in range(rows):
    workshop.append(input().split())

    if "Y" in workshop[row]:
        y_pos.append(row)
        y_pos.append(workshop[row].index("Y"))

    items += workshop[row].count("D")
    items += workshop[row].count("G")
    items += workshop[row].count("C")

command = input()

move_function = {
    "up": lambda x: ((x[0] - 1) % rows, x[1] % cols),
    "down": lambda x: ((x[0] + 1) % rows, x[1] % cols),
    "left": lambda x: (x[0] % rows, (x[1] - 1) % cols),
    "right": lambda x: (x[0] % rows, (x[1] + 1) % cols),
}

collected_items = {
    "D": 0,
    "G": 0,
    "C": 0,
}

while command != "End":
    move, steps = command.split('-')

    for _ in range(int(steps)):

        workshop[y_pos[0]][y_pos[1]] = 'x'
        y_pos[0], y_pos[1] = move_function[move](y_pos)
        symbol = workshop[y_pos[0]][y_pos[1]]

        if symbol in collected_items:
            collected_items[symbol] += 1
            items -= 1

            if items == 0:
                print("Merry Christmas!")
                break
    if items == 0:
        break

    command = input()

print(f"You've collected:\n- {collected_items['D']} Christmas decorations\n- {collected_items['G']} Gifts\n"
      f"- {collected_items['C']} Cookies")

workshop[y_pos[0]][y_pos[1]] = 'Y'
[print(' '.join(r)) for r in workshop]
