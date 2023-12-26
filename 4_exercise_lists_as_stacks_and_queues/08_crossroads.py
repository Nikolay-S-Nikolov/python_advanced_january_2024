from collections import deque

green_light = int(input())
free_window = int(input())

command = input()
line = deque()
cars_passed = 0
crash_happens = False

while command != 'END' and not crash_happens:
    green_counter = green_light
    difference = 0
    if command == 'green' and line:
        while line and green_counter!=0:
            car_name = line.popleft()
            if len(car_name) <= green_counter:
                green_counter -= len(car_name)
                cars_passed += 1
            else:
                difference = len(car_name) - green_counter
                if difference > free_window:
                    character_hit = car_name[green_counter + free_window]
                    crash_happens = True
                    print("A crash happened!")
                    print(f"{car_name} was hit at {character_hit}.")
                    break
                else:
                    cars_passed += 1
                    line.clear()
    else:
        line.append(command)
    command = input()
if not crash_happens:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
