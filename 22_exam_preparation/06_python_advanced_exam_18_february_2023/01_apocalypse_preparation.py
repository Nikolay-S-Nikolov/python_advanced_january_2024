from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

items_dict = {
    30: [0, 'Patch'],
    40: [0, 'Bandage'],
    100: [0, 'MedKit'],
}

while textiles and medicaments:

    textile = textiles.popleft()
    medicament = medicaments.pop()
    elements_sum = textile + medicament

    if elements_sum in items_dict.keys():
        items_dict[elements_sum][0] += 1

    elif elements_sum > 100:
        items_dict[100][0] += 1
        medicaments[-1] += elements_sum - 100

    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

else:
    if not textiles:
        print("Textiles are empty.")
    if not medicaments:
        print("Medicaments are empty.")

for amount_created, item_name in sorted(items_dict.values(), key=lambda x: (-x[0], x[1])):
    if amount_created:
        print(f"{item_name} - {amount_created}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(y) for y in medicaments[::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(y) for y in textiles)}")
