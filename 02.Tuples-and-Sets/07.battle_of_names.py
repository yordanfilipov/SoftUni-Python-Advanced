n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    current_sum = 0
    name = input()
    for ch in name:
        current_ord = ord(ch)
        current_sum += current_ord
    current_sum = int(current_sum / i)
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

if sum(odd_set) == sum(even_set):
    union_values = odd_set.intersection(even_set)
    print(*union_values, sep=", ")
elif sum(odd_set) > sum(even_set):
    different_values = odd_set.difference(even_set)
    print(*different_values, sep=", ")
else:
    symmetric_different_values = odd_set.symmetric_difference(even_set)
    print(*symmetric_different_values, sep=", ")