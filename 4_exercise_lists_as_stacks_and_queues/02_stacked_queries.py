stack = []
num_n = int(input())

for _ in range(num_n):
    command = input().split()
    action = command[0]
    if action == '1':
        number = int(command[1])
        stack.append(number)
    elif stack:
        if action == '2':
            stack.pop()
        elif action == '3':
            print(max(stack))
        elif action == '4':
            print(min(stack))
query_list = []

while stack:
    query_list.append(str(stack.pop()))

print(', '.join(query_list))
