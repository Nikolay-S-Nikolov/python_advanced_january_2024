odd_numbers = set()
even_numbers = set()

for row in range(int(input())):
    current_sum = sum(ord(letter) for letter in input()) // (row + 1)

    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)

sum_odd_set, sum_even_set = sum(odd_numbers), sum(even_numbers)

if sum_odd_set == sum_even_set:
    print(*odd_numbers.union(even_numbers), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=", ")
