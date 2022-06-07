from collections import deque

food_quantity = int(input())
orders = [int(el) for el in input().split()]
queue = deque(orders)
current_sum = 0

print(max(orders))

while len(queue) > 0:
    current_item = queue.popleft()
    current_sum += current_item
    if current_sum <= food_quantity:
        continue
    else:
        queue.insert(0, current_item)
        queue = list(queue)
        print(f"Orders left: {' '.join(map(str, queue))}")
        exit()

print(f"Orders complete")
