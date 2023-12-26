from collections import deque
from datetime import datetime, timedelta

robot_list = input().split(';')

robot_dict = {}
for robot in robot_list:
    k, v = robot.split('-')
    robot_dict[k] = [int(v), 0]

start_time = datetime.strptime(input(), "%H:%M:%S")

command = input()
product_deque = deque()
while command != 'End':
    product_deque.append(command)
    command = input()

while product_deque:
    start_time += timedelta(0, 1)
    free_robots = []
    for name, value in robot_dict.items():

        if value[1] != 0:
            value[1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        product_deque.rotate(-1)
        continue
    robot_name, data = free_robots[0]
    robot_dict[robot_name][1] = data[0]
    print(f"{robot_name} - {product_deque.popleft()} [{start_time.strftime('%H:%M:%S')}]")
