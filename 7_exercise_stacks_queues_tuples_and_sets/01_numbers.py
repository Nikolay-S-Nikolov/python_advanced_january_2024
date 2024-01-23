first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    action, set_name, *numbers = input().split()

    if action == 'Add':
        if set_name == "First":
            [first_set.add(int(num)) for num in numbers]
        elif set_name == "Second":
            [second_set.add(int(num)) for num in numbers]

    elif action == 'Remove':
        if set_name == "First":
            [first_set.discard(int(num)) for num in numbers]
        elif set_name == "Second":
            [second_set.discard(int(num)) for num in numbers]

    elif action == 'Check':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


# Second solution
#
# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first_set.add(int(num)) for num in x],
#     "Add Second": lambda x: [second_set.add(int(num)) for num in x],
#     "Remove First": lambda x: [first_set.discard(int(num)) for num in x],
#     "Remove Second": lambda x: [second_set.discard(int(num)) for num in x],
#     "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
# }
#
# for _ in range(int(input())):
#     action, set_name, *numbers = input().split()
#     command = action + " " + set_name
#     functions[command](numbers)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")
