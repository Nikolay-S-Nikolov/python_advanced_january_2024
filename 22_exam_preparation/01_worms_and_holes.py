from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

initial_worm_count = len(worms)
matches_count = 0

while worms and holes:
    worm = worms.pop()

    if worm <= 0:
        continue
    hole = holes.popleft()

    if worm == hole:
        matches_count += 1

    else:
        worms.append(worm - 3)

print(f"Matches: {matches_count}") if matches_count else print("There are no matches.")

if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

else:
    if matches_count == initial_worm_count:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

print(f"Holes left: {', '.join(str(x) for x in holes)}") if holes else print("Holes left: none")

