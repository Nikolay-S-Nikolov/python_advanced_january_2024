n, m = list(map(int, input().split()))

first_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}

# intersection_set = first_set.intersection(second_set)
intersection_set = first_set & second_set

print(*intersection_set, sep='\n')
