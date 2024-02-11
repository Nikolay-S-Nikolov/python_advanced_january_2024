from collections import deque


def duck_distribution(programmer_time):
    for time_range in rubber_ducks_type.keys():
        if programmer_time in time_range:
            rubber_ducks_type[time_range][0] += 1


programmers_time = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

rubber_ducks_type = {
    range(61): [0, 'Darth Vader Ducky'],
    range(61, 121): [0, 'Thor Ducky'],
    range(121, 181): [0, 'Big Blue Rubber Ducky'],
    range(181, 241): [0, 'Small Yellow Rubber Ducky'],
}
while programmers_time:

    time = programmers_time.popleft()
    task = number_of_tasks.pop()
    calculated_time = time * task

    if calculated_time > 240:
        number_of_tasks.append(task - 2)
        programmers_time.append(time)
        continue

    duck_distribution(calculated_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

[print(f"{duck_type}: {count}") for count, duck_type in rubber_ducks_type.values()]
