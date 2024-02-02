rover_pos = []
mars = []

for row in range(6):
    mars.append(input().split())

    if "E" in mars[row]:
        rover_pos.append(row)
        rover_pos.append(mars[row].index("E"))

commands = input().split(', ')

commands_dict = {
    "up": lambda x: ((x[0] - 1) % 6, x[1]),
    "down": lambda x: ((x[0] + 1) % 6, x[1]),
    "left": lambda x: (x[0], (x[1] - 1) % 6),
    "right": lambda x: (x[0], (x[1] + 1) % 6)
}

water_found = False
metal_found = False
concrete_found = False

for move in commands:

    rover_pos = commands_dict[move](rover_pos)
    rover_lands_position = mars[rover_pos[0]][rover_pos[1]]

    if rover_lands_position == "W":
        print(f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        water_found = True

    elif rover_lands_position == "M":
        print(f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        metal_found = True

    elif rover_lands_position == "C":
        print(f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        concrete_found = True

    elif rover_lands_position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if metal_found and concrete_found and water_found:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
