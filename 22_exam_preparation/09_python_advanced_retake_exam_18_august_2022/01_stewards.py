from collections import deque

seats = input().split(', ')
first_seq = deque(int(x) for x in input().split(', '))
second_seq = deque(int(x) for x in input().split(', '))

seat_matches = []
rotation_count = 0

while rotation_count != 10 and len(seat_matches) != 3:

    rotation_count += 1
    first_number = first_seq.popleft()
    last_number = second_seq.pop()
    letter = chr(first_number + last_number)

    if str(first_number) + letter in seats and str(first_number) + letter not in seat_matches:
        seat_matches.append(str(first_number) + letter)

    elif str(last_number) + letter in seats and str(last_number) + letter not in seat_matches:
        seat_matches.append(str(last_number) + letter)

    else:
        first_seq.append(first_number)
        second_seq.appendleft(last_number)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotation_count}")
