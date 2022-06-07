clothes = [int(el) for el in input().split()]
capacity = int(input())

racks = 1
current_capacity = capacity

while len(clothes) > 0:
    current_clothes = clothes.pop()
    if current_clothes <= current_capacity:
        current_capacity -= current_clothes
    else:
        racks += 1
        current_capacity = capacity
        current_capacity -= current_clothes
print(racks)