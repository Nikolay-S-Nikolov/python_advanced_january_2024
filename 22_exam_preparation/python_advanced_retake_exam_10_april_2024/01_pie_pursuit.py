from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while pies and contestants:
    current_contestants = contestants.popleft()
    current_pies = pies.pop()

    if current_contestants >= current_pies:
        if current_contestants - current_pies == 0:
            continue
        contestants.append(current_contestants - current_pies)
    else:
        pieces_left = current_pies-current_contestants
        if pieces_left == 1 and pies:
            pies[-1] += 1
            continue
        pies.append(pieces_left)

if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif not contestants and not pies:
    print("We have a champion!")
else:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
