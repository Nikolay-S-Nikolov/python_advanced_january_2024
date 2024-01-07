def fill_the_box(*data):
    cube_volume = data[0] * data[1] * data[2]

    for idx in range(3, len(data)):

        if data[idx] == 'Finish':
            break

        if cube_volume - data[idx] < 0:
            current_cubes_left = data[idx] - cube_volume
            return f"No more free space!" \
                   f" You have " \
                   f"{current_cubes_left +sum(data[i] for i in range(idx+1, len(data)) if data[i] != 'Finish')}" \
                   f" more cubes."

        cube_volume -= data[idx]

    return f"There is free space in the box. You could put {cube_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
