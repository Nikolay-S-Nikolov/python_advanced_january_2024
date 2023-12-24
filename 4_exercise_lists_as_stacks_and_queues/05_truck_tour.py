from collections import deque

num_petrol_pumps = int(input())
tour_deque = deque()

for _ in range(num_petrol_pumps):
    tour_deque.append([int(x) for x in input().split()])

start_idx = 0
count = 0
while count < num_petrol_pumps:
    total_petrol = 0
    for idx in range(num_petrol_pumps):
        petrol, distance = tour_deque[idx]
        total_petrol += petrol
        if distance > total_petrol:
            tour_deque.rotate(-1)
            start_idx += 1
            count = 0
            break
        total_petrol -= distance
        count += 1

print(start_idx)
