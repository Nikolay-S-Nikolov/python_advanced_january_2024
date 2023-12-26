from collections import deque
from datetime import datetime, timedelta

robot_dict = {r.split('-')[0]: [int(r.split('-')[1]), 0] for r in input().split(';')}
start_time = datetime.strptime(input(), "%H:%M:%S")

command = input()
product_deque = deque()
while command != 'End':
    product_deque.append(command)
    command = input()

while product_deque:
    start_time += timedelta(0, 1)
    robot_dict = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robot_dict.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robot_dict.items()))
    if not free_robots:
        product_deque.rotate(-1)
        continue

    robot_dict[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {product_deque.popleft()} [{start_time.strftime('%H:%M:%S')}]")
