from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_litters_of_water = []

while cups and bottles:
    current_cup = cups[0]
    while bottles:
        current_bottles = bottles.pop()
        current_cup -= current_bottles
        if current_cup <= 0:
            wasted_litters_of_water.append(-current_cup)
            cups.popleft()
            break

if not cups and bottles:
    bottles_list = []
    while bottles:
        bottles_list.append(str(bottles.pop()))
    print(f"Bottles: {' '.join(bottles_list)}")
else:
    cups_list = []
    while cups:
        cups_list.append(str(cups.popleft()))
    print(f"Cups: {' '.join(cups_list)}")

print(f"Wasted litters of water: {sum(wasted_litters_of_water)}")
