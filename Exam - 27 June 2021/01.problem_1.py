from collections import deque

chocolates = deque([int(el) for el in input().split(", ")])
cups_of_milk = deque([int(el) for el in input().split(", ")])

milkshakes = 0

while True:
    if not chocolates or not cups_of_milk or milkshakes >= 5:
        break

    last_chocolate = chocolates[-1]
    first_cup_of_milk = cups_of_milk[0]

    if first_cup_of_milk <= 0 or last_chocolate <= 0:
        if first_cup_of_milk <= 0:
            cups_of_milk.popleft()
        if last_chocolate <= 0:
            chocolates.pop()
        continue

    if last_chocolate == first_cup_of_milk:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.append(first_cup_of_milk)
        cups_of_milk.popleft()
        chocolates[-1] -= 5
        if chocolates[-1] <= 0:
            chocolates.pop()

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join([str(el) for el in cups_of_milk])}")
else:
    print("Milk: empty")