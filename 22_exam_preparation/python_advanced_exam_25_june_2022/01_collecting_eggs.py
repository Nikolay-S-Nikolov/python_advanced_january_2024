from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]
boxes = 0

while eggs and papers:

    egg = eggs.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    paper = papers.pop()

    if (egg + paper) <= 50:
        boxes += 1

print(f"Great! You filled {boxes} boxes.") if boxes else print("Sorry! You couldn't fill any boxes!")

print(f"Eggs left: {', '.join(str(x) for x in eggs)}") if eggs else None

print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}") if papers else None
