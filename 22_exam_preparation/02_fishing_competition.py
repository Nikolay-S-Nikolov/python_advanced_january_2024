QUOTA = 20
SIZE = int(input())

fishing_area = []
ship_pos = []
caught_fish = 0

for row in range(SIZE):
    fishing_area.append(list(input()))

    if 'S' in fishing_area[row]:
        ship_pos.append(row)
        ship_pos.append(fishing_area[row].index('S'))

move_dict = {
    "up": lambda x: ((x[0] - 1) % SIZE, x[1]),
    "down": lambda x: ((x[0] + 1) % SIZE, x[1]),
    "left": lambda x: (x[0], (x[1] - 1) % SIZE),
    "right": lambda x: (x[0], (x[1] + 1) % SIZE)
}

command = input()
while command != "collect the nets":

    fishing_area[ship_pos[0]][ship_pos[1]] = '-'
    ship_pos = move_dict[command](ship_pos)
    r, c = ship_pos

    if fishing_area[r][c] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{ship_pos[0]},{ship_pos[1]}]")
        raise SystemExit

    caught_fish += int(fishing_area[r][c]) if fishing_area[r][c] != "-" else 0

    fishing_area[r][c] = "S"
    command = input()

print(f"Success! You managed to reach the quota!") if caught_fish >= QUOTA else print(
    f"You didn't catch enough fish and didn't reach the quota! "
    f"You need {QUOTA - caught_fish} tons of fish more.")

print(f"Amount of fish caught: {caught_fish} tons.") if caught_fish > 0 else None

[print(f"{''.join(row)}") for row in fishing_area]
