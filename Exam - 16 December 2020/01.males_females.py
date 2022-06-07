from collections import deque

males = deque([int(el) for el in input().split() if int(el) > 0])
females = deque([int(el) for el in input().split() if int(el) > 0])

matches = 0

while True:
    if not females or not males:
        break
    first_female = females[0]
    last_male = males[-1]

    if first_female == last_male:
        females.popleft()
        males.pop()
        matches += 1
    elif first_female % 25 == 0:
        females.popleft()
        females.popleft()
    elif last_male % 25 == 0:
        males.pop()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(reversed([str(el) for el in males]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")

# while True:
#     if not males or not females:
#         break
#     last_male = males[-1]
#     first_female = females[0]
#
#     if first_female % 25 == 0:
#         females.popleft()
#         if not females:
#             continue
#         females.popleft()
#     if last_male % 25 == 0:
#         males.pop()
#         if not males:
#             continue
#         males.pop()
#
#     if not males or not females:
#         break
#     if first_female == last_male:
#         males.pop()
#         females.popleft()
#         matches += 1
#     else:
#         females.popleft()
#         last_male -= 2
#         males.pop()
#         if last_male > 0:
#             males.append(last_male)