def list_manipulator(nums, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            # if args[2]:
            numbers = args[:1:-1]
            for i in range(len(numbers)):
                nums.insert(0, numbers[i])
        elif args[1] == "end":
            numbers = args[2:]
            for i in range(len(numbers)):
                nums.append(numbers[i])
    elif args[0] == "remove":
        if args[1] == "beginning":
            try:
                if args[2]:
                    for _ in range(int(args[2])):
                        nums.pop(0)
            except:
                nums.pop(0)
        elif args[1] == "end":
            try:
                if args[2]:
                    for _ in range(int(args[2])):
                        nums.pop()
            except:
                nums.pop()
    return nums

print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
