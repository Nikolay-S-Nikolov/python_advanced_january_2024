n = int(input())

reservation = set()

for _ in range(n):
    reservation.add(input())

command = input()
while command != 'END':

    reservation.discard(command)
    command = input()

print(len(reservation))
print(*sorted(reservation), sep='\n')
