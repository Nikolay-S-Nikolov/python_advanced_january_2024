from collections import deque

quantity_of_food = int(input())
quantity_food_orders = deque([int(x) for x in input().split()])
print(max(quantity_food_orders))

a=6
while True:
    if not quantity_food_orders:
        print("Orders complete")
        break
    food_to_serv = quantity_food_orders[0]
    if food_to_serv <= quantity_of_food:
        quantity_of_food -= food_to_serv
        quantity_food_orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in quantity_food_orders])}")
        break
