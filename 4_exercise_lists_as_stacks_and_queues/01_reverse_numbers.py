n_integers = input().split()
stack = []
while n_integers:
    stack.append(n_integers.pop())
print(" ".join(stack))
