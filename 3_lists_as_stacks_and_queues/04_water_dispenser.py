from collections import deque

quantity_of_water = int(input())
water_queue = deque()
name = input()
while name != 'Start':
    water_queue.append(name)
    name = input()

command = input()

while command != 'End':
    action = command.split()
    if len(action) == 1:
        person_name = water_queue.popleft()
        water_to_get = int(action[0])
        if water_to_get <= quantity_of_water:
            quantity_of_water -= water_to_get
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        water_to_refill = int(action[1])
        quantity_of_water += water_to_refill
    command = input()

print(f"{quantity_of_water} liters left")
