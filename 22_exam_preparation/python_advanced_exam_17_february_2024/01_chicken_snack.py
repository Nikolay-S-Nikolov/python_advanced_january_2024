from collections import deque

money_in_pocket = [int(x) for x in input().split()]
prices_of_foods = deque(int(x) for x in input().split())
food_eaten = 0

while money_in_pocket and prices_of_foods:

    last_money = money_in_pocket.pop()
    first_price = prices_of_foods.popleft()

    if last_money == first_price:
        food_eaten += 1

    elif last_money > first_price:
        change = last_money - first_price
        food_eaten += 1
        if money_in_pocket:
            money_in_pocket[-1] += change
        else:
            money_in_pocket.append(change)

if food_eaten:
    if food_eaten >= 4:
        print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
    elif 1 < food_eaten < 4:
        print(f"Henry ate: {food_eaten} foods.")
    else:
        print(f"Henry ate: {food_eaten} food.")

else:
    print("Henry remained hungry. He will try next weekend again.")
