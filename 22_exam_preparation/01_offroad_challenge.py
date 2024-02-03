from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())

top_altitude = 4
reached = []

for num in range(1, 5):

    if (initial_fuel[-1] - additional_consumption_index[0]) < amount_of_fuel_needed[0]:
        print(f"John did not reach: Altitude {num}")
        break

    initial_fuel.pop()
    additional_consumption_index.popleft()
    amount_of_fuel_needed.popleft()

    print(f"John has reached: Altitude {num}")
    reached.append("Altitude " + str(num))

if reached:
    if amount_of_fuel_needed:
        print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached)}")

    else:
        print(f"John has reached all the altitudes and managed to reach the top!")

else:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
