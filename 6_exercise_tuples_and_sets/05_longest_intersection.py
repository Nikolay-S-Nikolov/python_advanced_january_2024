longest_intersection = []

for _ in range(int(input())):

    [first_start, first_end], [second_start, second_end] = [el.split(',') for el in input().split('-')]

    current_intersection = set(range(int(first_start), int(first_end) + 1)).intersection(
        range(int(second_start), int(second_end) + 1))

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = list(current_intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

# Solution 2 only with lists

# longest_intersection = []
#
# for _ in range(int(input())):
#
#     [first_start, first_end], [second_start, second_end] = [el.split(',') for el in input().split('-')]
#
#     start_set = max(int(first_start), int(second_start))
#     stop_set = min(int(first_end), int(second_end))
#
#     current_set = list(range(start_set, stop_set + 1))
#
#     if len(current_set) > len(longest_intersection):
#         longest_intersection = current_set
#
# print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
