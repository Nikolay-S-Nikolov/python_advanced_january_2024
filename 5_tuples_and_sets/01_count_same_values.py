numbers = tuple(map(float, input().split()))

occurrences = {}
for number in numbers:
    if number not in occurrences:
        occurrences[number] = numbers.count(number)

for num, count in occurrences.items():
    print(f"{num} - {count} times")
