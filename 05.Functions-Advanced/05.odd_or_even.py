command = input()
numbers = [int(el) for el in input().split()]

if command == "Odd":
    print(sum([int(el) for el in numbers if el % 2 == 1]) * len(numbers))
else:
    print(sum([int(el) for el in numbers if el % 2 == 0]) * len(numbers))
