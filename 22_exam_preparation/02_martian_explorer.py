from collections import deque


def move_rover(direction: str, pos: list):
    position = commands_dict[direction](pos)
    position_dict = {-1: 5,
                     0: 0,
                     1: 1,
                     2: 2,
                     3: 3,
                     4: 4,
                     5: 5,
                     6: 0,
                     }
    new_pos = [position_dict[position[0]], position_dict[position[1]]]

    return new_pos


rover_pos = []
mars = []

for row in range(6):
    mars.append(input().split())

    if "E" in mars[row]:
        rover_pos.append(row)
        rover_pos.append(mars[row].index("E"))

commands = deque(input().split(', '))

commands_dict = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1)
}

water_found = False
metal_found = False
concrete_found = False

while commands:

    move = commands.popleft()
    # mars[rover_pos[0]][rover_pos[1]] = "-"
    rover_pos = move_rover(move, rover_pos)
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
