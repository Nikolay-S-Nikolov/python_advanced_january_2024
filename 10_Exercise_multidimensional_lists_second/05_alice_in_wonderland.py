n = int(input())

territory = []
alice_pos = []

for row in range(n):
    territory.append(input().split())

    if 'A' in territory[row]:
        alice_pos = [row, territory[row].index('A')]
        territory[row][alice_pos[1]] = '*'
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

tea_bags_collected = 0

while tea_bags_collected < 10:
    alice_movement = input()

    row, col = directions[alice_movement][0] + alice_pos[0], directions[alice_movement][1] + alice_pos[1]

    if not {row, col}.issubset(range(n)):
        break
    if territory[row][col] == 'R':
        territory[row][col] = '*'
        break
    if territory[row][col].isdigit():
        tea_bags_collected += int(territory[row][col])

    territory[row][col] = '*'
    alice_pos = [row, col]

if tea_bags_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(' '.join(element)) for element in territory]
