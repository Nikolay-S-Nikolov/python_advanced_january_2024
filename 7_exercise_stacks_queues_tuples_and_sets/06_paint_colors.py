from collections import deque

substring_deque = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_color_check = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}
collected_colors = []

while substring_deque:
    first_substring = substring_deque.popleft()
    last_substring = substring_deque.pop() if substring_deque else ""

    for color in (first_substring + last_substring, last_substring + first_substring):
        if color in colors:
            collected_colors.append(color)
            break
    else:
        for el in (first_substring[:-1], last_substring[:-1]):
            if el:
                substring_deque.insert(len(substring_deque) // 2, el)

for color in set(collected_colors).intersection(set(secondary_color_check.keys())):
    if not secondary_color_check[color].issubset(set(collected_colors)):
        collected_colors.remove(color)

print(collected_colors)

# from collections import deque
#
# substring_deque = deque(input().split())
#
# colors = {"red", "yellow", "blue", "orange", "purple", "green"}
# collected_colors = []
#
# while len(substring_deque) > 1:
#     first_substring = substring_deque.popleft()
#     last_substring = substring_deque.pop()
#
#     if {first_substring + last_substring}.issubset(colors):
#         collected_colors.append(first_substring + last_substring)
#
#     elif {last_substring + first_substring}.issubset(colors):
#         collected_colors.append(last_substring + first_substring)
#
#     else:
#         substring_deque.insert(len(substring_deque) // 2, last_substring[:-1]) if last_substring[:-1] != '' else None
#         substring_deque.insert(len(substring_deque) // 2, first_substring[:-1]) if first_substring[:-1] != '' else None
#
# if len(substring_deque) == 1:
#     last_string = substring_deque.pop()
#
#     while last_string:
#
#         if {last_string}.issubset(colors):
#             collected_colors.append(last_string)
#             break
#
#         else:
#             last_string = last_string[:-1]
#
# secondary_color_check = {
#     "orange": {"red", "yellow"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"}
# }
#
# for color in collected_colors:
#     if color in secondary_color_check and not secondary_color_check[color].issubset(set(collected_colors)):
#         collected_colors.remove(color)
#
# print(collected_colors)
