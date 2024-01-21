num_names = int(input())

unique_names = set()

for _ in range(num_names):
    unique_names.add(input())

print(*unique_names, sep="\n")
