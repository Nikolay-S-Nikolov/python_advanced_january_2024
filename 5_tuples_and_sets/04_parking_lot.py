number_of_commands = int(input())

parking_lot = set()

for _ in range(number_of_commands):
    command, car_number = input().split(", ")
    if command == 'IN':
        parking_lot.add(car_number)
    elif command == 'OUT':
        parking_lot.discard(car_number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    print(*parking_lot, sep='\n')
