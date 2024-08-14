from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    defenders = bees.popleft()
    attackers = bee_eaters.pop()

    while True:

        defenders -= 7
        if defenders < 0:
            bee_eaters.append(attackers)
            break

        attackers -= 1
        if attackers == 0:
            if defenders > 0:
                bees.append(defenders)
            break

print("The final battle is over!")

if bees:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")
else:
    print("But no one made it out alive!")
