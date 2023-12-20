expression = input()
stack = []
for idx in range(len(expression)):
    if expression[idx] == "(":
        stack.append(idx)
    elif expression[idx] == ')':
        end_idx = idx + 1
        start_idx = stack.pop()
        print(expression[start_idx: end_idx])

