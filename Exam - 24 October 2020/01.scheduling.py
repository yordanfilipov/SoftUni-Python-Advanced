from collections import deque

jobs = [int(el) for el in input().split(", ")]
index = int(input())

searched_number = jobs[index]
sorted_jobs = deque(sorted(jobs))
cycles_sum = 0

while True:
    if not sorted_jobs:
        break
    current_number = sorted_jobs.popleft()
    if current_number > searched_number:
        break
    cycles_sum += current_number

print(cycles_sum)