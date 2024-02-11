from collections import deque

monsters_armor = deque(int(x) for x in input().split(','))
striking_impact = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters_armor and striking_impact:
    monster = monsters_armor.popleft()
    strike = striking_impact.pop()

    if strike >= monster:
        strike -= monster
        killed_monsters += 1

        if not striking_impact and strike > 0:
            striking_impact.append(strike)
        elif striking_impact:
            striking_impact[-1] += strike

    else:
        monster -= strike
        monsters_armor.append(monster)

if not monsters_armor:
    print("All monsters have been killed!")

if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
