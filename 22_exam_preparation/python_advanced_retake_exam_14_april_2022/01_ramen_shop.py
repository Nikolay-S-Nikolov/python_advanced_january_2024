from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customers:

    if bowls_of_ramen[-1] > customers[0]:
        first_customer = customers.popleft()
        bowls_of_ramen[-1] -= first_customer
        continue

    if bowls_of_ramen[-1] < customers[0]:
        last_bowl = bowls_of_ramen.pop()
        customers[0] -= last_bowl
        continue

    first_customer = customers.popleft()
    last_bowl = bowls_of_ramen.pop()

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(list(map(str, customers)))}")
else:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(list(map(str, bowls_of_ramen)))}")
