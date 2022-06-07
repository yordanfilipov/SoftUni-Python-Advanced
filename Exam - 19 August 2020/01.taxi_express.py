from collections import deque

customers = deque([int(el) for el in input().split(', ')])
# how much time it takes to drive the customer to his/her destination

taxis = deque([int(el) for el in input().split(', ')])
# how much time they can drive, before they need to refill their tanks

total_time = 0

while True:
    if not customers or not taxis:
        break
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    customers = [str(el) for el in customers]
    print(f"Customers left: {', '.join(customers)}")
