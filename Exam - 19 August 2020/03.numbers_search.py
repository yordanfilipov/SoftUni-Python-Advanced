def numbers_searching(*args):
    numbers = list(args)
    duplicate_nums = sorted(list(set([x for x in numbers if numbers.count(x) > 1])))
    missing_number = 0
    numbers = sorted(list(set(numbers)))
    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i + 1] - 1:
            missing_number = numbers[i] + 1
            break
    return [missing_number, duplicate_nums]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))