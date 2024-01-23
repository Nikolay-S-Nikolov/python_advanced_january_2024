from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

toy_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_toys = []

while materials and magic_levels:

    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    total_magic_level = material * magic_level

    if toy_table.get(total_magic_level):
        crafted_toys.append(toy_table[total_magic_level])
    elif total_magic_level < 0:
        materials.append(material + magic_level)
    elif total_magic_level > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]


