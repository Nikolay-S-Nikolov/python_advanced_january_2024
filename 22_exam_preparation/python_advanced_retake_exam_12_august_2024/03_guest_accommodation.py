from collections import deque


def accommodate(*args, **available_rooms):
    guest_groups = deque(args)

    not_accommodated = 0
    accommodated_rooms = {}

    while guest_groups:

        group = guest_groups.popleft()

        for room_num, capacity in sorted(available_rooms.items(), key=lambda x: (x[1], x[0])):

            if capacity >= group:
                num_of_room = room_num.split('_')[1]
                accommodated_rooms[num_of_room] = group

                del available_rooms[room_num]
                break
        else:
            not_accommodated += group

    if accommodated_rooms:

        result = [f"A total of {len(accommodated_rooms)} accommodations were completed!"]
        sorted_rooms = sorted(accommodated_rooms.items(), key=lambda x: x[0])
        result.extend(
            [f'<Room {room_number} accommodates {guests} guests>' for room_number, guests in sorted_rooms]
        )
    else:
        result = ["No accommodations were completed!"]

    if not_accommodated:
        result.append(f"Guests with no accommodation: {not_accommodated}")

    if available_rooms:
        result.append(f"Empty rooms: {len(available_rooms)}")

    return '\n'.join(result)
