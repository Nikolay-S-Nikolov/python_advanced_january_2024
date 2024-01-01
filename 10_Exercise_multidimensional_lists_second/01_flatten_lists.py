matrix = [x.split() for x in input().split('|')[::-1]]

[print(*el, end=' ') for el in matrix if el]
