from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_deque = deque(int(x) for x in input().split())
lock_deque = deque(int(x) for x in input().split())
intelligence_value = int(input())
initial_bullet_number = len(bullets_deque)
reload_counter = 0

while bullets_deque and lock_deque:
    current_lock = lock_deque[0]
    lock_destroyed = False
    while not lock_destroyed and bullets_deque:

        current_bullet = bullets_deque.pop()
        reload_counter += 1
        if current_bullet <= current_lock:
            print("Bang!")
            lock_destroyed = True
            lock_deque.popleft()
        else:
            print("Ping!")
        if reload_counter == barrel_size and bullets_deque:
            print("Reloading!")
            reload_counter = 0
if lock_deque:
    print(f"Couldn't get through. Locks left: {len(lock_deque)}")
else:
    money_earned = intelligence_value - (initial_bullet_number - len(bullets_deque)) * bullet_price
    print(f"{len(bullets_deque)} bullets left. Earned ${money_earned}")
