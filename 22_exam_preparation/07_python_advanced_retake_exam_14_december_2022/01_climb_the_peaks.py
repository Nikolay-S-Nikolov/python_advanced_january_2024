from collections import deque

food_portions = [int(x) for x in input().split(', ')]
stamina_quantities = deque(int(x) for x in input().split(', '))

peaks_difficulty = [
    ('Kamenitza', 70),
    ('Polezhan', 60),
    ('Banski Suhodol', 100),
    ('Kutelo', 90),
    ('Vihren', 80)
]

conquered_peaks = []
days = 0

while peaks_difficulty and food_portions:
    days += 1

    if days == 8:
        break

    peak_name, peak_difficulty = peaks_difficulty[-1]
    food = food_portions.pop()
    stamina = stamina_quantities.popleft()

    if (food + stamina) >= peak_difficulty:
        conquered_peaks.append(peak_name)
        peaks_difficulty.pop()

if peaks_difficulty:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conquered_peaks:
    nl = '\n'
    print(f"Conquered peaks:\n{nl.join(conquered_peaks)}")
