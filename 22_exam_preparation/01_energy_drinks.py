from collections import deque

milligrams_of_coffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

total_caffeine = 0
while milligrams_of_coffeine and energy_drinks:
    coffeine = milligrams_of_coffeine.pop()
    drink = energy_drinks.popleft()
    coffeine_sum = coffeine * drink

    if coffeine_sum <= 300 - total_caffeine:
        total_caffeine += coffeine_sum
    else:
        total_caffeine -= 30 if total_caffeine - 30 >= 0 else 0
        energy_drinks.append(drink)

if energy_drinks:
    print(f"Drinks left: {', '.join(list(map(str, energy_drinks)))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
