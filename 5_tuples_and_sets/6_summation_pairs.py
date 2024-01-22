import time

unique_numbers = list(map(int, input().split()))
target_number = int(input())

start = time.time()
paired_numbers = set()
for i in range(len(unique_numbers)):
    if {unique_numbers[i]}.issubset(paired_numbers) or unique_numbers[i] > target_number:
        continue
    for j in range(i + 1, len(unique_numbers)):
        if not {unique_numbers[j]}.issubset(paired_numbers) and unique_numbers[j] <= target_number:
            if (unique_numbers[i] + unique_numbers[j]) == target_number:
                print(f"{unique_numbers[i]} + {unique_numbers[j]} = {target_number}")
                paired_numbers.add(unique_numbers[i])
                paired_numbers.add(unique_numbers[j])
                break
end = time.time()
print(f"Time range:{(end - start):.11f}")
