from collections import deque

customer_name = deque()
command = input()

while command != 'End':
    if command == 'Paid':
        while customer_name:
            print(customer_name.popleft())
    else:
        customer_name.append(command)
    command = input()
print(f"{len(customer_name)} people remaining.")
