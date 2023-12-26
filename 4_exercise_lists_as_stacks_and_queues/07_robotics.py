from collections import deque


def formatted_time(time_seconds):
    hours = time_seconds // 3600
    minutes = (time_seconds % 3600) // 60
    sec = (time_seconds % 3600) % 60
    if hours > 23:
        hours = 0
    return f'[{hours:02d}:{minutes:02d}:{sec:02d}]'


robot_list = input().split(';')

robot_dict = {}
for robot in robot_list:
    k, v = robot.split('-')
    robot_dict[k] = [int(v), 0]

start_time = [int(x) for x in input().split(':')]
start_time_in_seconds = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]

command = input()
product_deque = deque()
while command != 'End':
    product_deque.append(command)
    command = input()

while product_deque:
    start_time_in_seconds += 1
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
    print(f"{robot_name} - {product_deque.popleft()} {formatted_time(start_time_in_seconds)}")
