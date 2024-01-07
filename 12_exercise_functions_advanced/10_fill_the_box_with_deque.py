from collections import deque


def fill_the_box(height, length, width, *data):
    cube_volume = height * length * width
    data = deque(data)

    while data[0] != 'Finish':
        cube_volume -= data.popleft()

        if cube_volume < 0:
            return f"No more free space!" \
                   f" You have " \
                   f"{-cube_volume + sum(data[i] for i in range(len(data)) if data[i] != 'Finish')}" \
                   f" more cubes."

    return f"There is free space in the box. You could put {cube_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
