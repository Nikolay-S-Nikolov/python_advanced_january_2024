n = int(input())
chemical_elements_list = []

for _ in range(n):
    chemical_elements_list.extend(input().split())

print(*set(chemical_elements_list), sep='\n')
