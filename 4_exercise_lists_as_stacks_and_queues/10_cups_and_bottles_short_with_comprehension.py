from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_litters_of_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottles = bottles.pop()
    if current_cup <= current_bottles:
        wasted_litters_of_water += current_bottles - current_cup
    else:
        cups.appendleft(current_cup - current_bottles)

if not cups and bottles:
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")
else:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")

print(f"Wasted litters of water: {wasted_litters_of_water}")
