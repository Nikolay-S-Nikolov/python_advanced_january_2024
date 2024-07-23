from collections import deque

materials = [int(x) for x in input().split()]

magic_level = deque(int(x) for x in input().split())

presents = {}

while materials and magic_level:
    last_material = materials.pop()
    magic = magic_level.popleft()

    product = last_material + magic

    if product < 100:
        if product % 2 == 0:
            product = last_material * 2 + magic * 3
        else:
            product *= 2
    elif product > 499:
        product /= 2

    if 100 <= product < 200:
        if 'Gemstone' not in presents:
            presents['Gemstone'] = 0
        presents['Gemstone'] += 1
    elif 200 <= product < 300:
        if 'Porcelain Sculpture' not in presents:
            presents['Porcelain Sculpture'] = 0
        presents['Porcelain Sculpture'] += 1
    elif 300 <= product < 400:
        if 'Gold' not in presents:
            presents['Gold'] = 0
        presents['Gold'] += 1
    elif 400 <= product < 500:
        if 'Diamond Jewellery' not in presents:
            presents['Diamond Jewellery'] = 0
        presents['Diamond Jewellery'] += 1

if ('Gemstone' in presents and 'Porcelain Sculpture' in presents) or (
        'Gold' in presents and 'Diamond Jewellery' in presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for k, v in sorted(presents.items(), key=lambda p: p[0]):
    print(f"{k}: {v}")
