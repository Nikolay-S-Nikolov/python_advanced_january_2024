from collections import deque

COOKIES = 1

elves_energy = deque(int(x) for x in input().split())
materials_in_box = deque(int(x) for x in input().split())

total_number_of_toys = 0
total_used_energy = 0
count = 0

while elves_energy and materials_in_box:
    current_elf_energy = elves_energy.popleft()

    if current_elf_energy < 5:
        continue

    current_box = materials_in_box[-1]
    count += 1
    current_toys = 0

    if count % 3 == 0:
        current_toys += 1
        current_box *= 2

    if current_elf_energy - current_box >= 0:
        total_used_energy += current_box
        current_elf_energy -= current_box

        if count % 5 == 0:
            current_toys = 0
        else:
            current_elf_energy += COOKIES
            current_toys += 1
        materials_in_box.pop()
    else:
        current_elf_energy *= 2
        current_toys = 0

    total_number_of_toys += current_toys
    elves_energy.append(current_elf_energy)

print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")

if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")

