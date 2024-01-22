# n = int(input())
#
# unique_username = set()
#
# for _ in range(n):
#     unique_username.add(input())
#
# print(*unique_username, sep='\n')

# Solution 2
print(*{input() for _ in range(int(input()))}, sep='\n')
