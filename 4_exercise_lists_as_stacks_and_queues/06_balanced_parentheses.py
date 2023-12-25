from collections import deque

sequence_deque = deque(input())

while sequence_deque and len(sequence_deque) != 1:
    left_par = sequence_deque[0]
    right_par = sequence_deque[-1]
    second_par = sequence_deque[1]
    if (left_par == '{' and second_par == '}') or (left_par == '(' and second_par == ')') \
            or (left_par == '[' and second_par == ']'):
        sequence_deque.popleft()
        sequence_deque.popleft()
    elif (left_par == '{' and right_par == '}') or (left_par == '(' and right_par == ')') \
            or (left_par == '[' and right_par == ']'):
        sequence_deque.popleft()
        sequence_deque.pop()
    else:
        break

if sequence_deque:
    print('NO')
else:
    print('YES')
