from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:

    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)

    else:
        tools.append(tool + 1)
        substance -= 1

        if substance > 0:
            substances.append(substance)

print("Harry found an ostracon, which is dated to the 6th century BCE.") if not challenges \
    else print("Harry is lost in the temple. Oblivion awaits him.")

print(f"Tools: {', '.join(str(x) for x in tools)}") if tools else None

print(f"Substances: {', '.join(str(x) for x in substances)}") if substances else None

print(f"Challenges: {', '.join(str(x) for x in challenges)}") if challenges else None
