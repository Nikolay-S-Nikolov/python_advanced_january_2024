clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())
sum_clothes = 0
number_of_racks = 1

while clothes_in_box:
    current_clothes_pile = clothes_in_box.pop()
    if sum_clothes + current_clothes_pile > rack_capacity:
        number_of_racks += 1
        sum_clothes = 0
    sum_clothes += current_clothes_pile

print(number_of_racks)
