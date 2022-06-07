from collections import deque


def math_operations(*args, **kwargs):
    print(type(args))
    nums = deque([int(el) for el in args])
    operations_dict = {}
    for letter, value in kwargs.items():
        operations_dict[letter] = value
    while nums:
        if nums:
            current_num = nums.popleft()
            operations_dict['a'] += current_num
        if nums:
            current_num = nums.popleft()
            operations_dict['s'] -= current_num
        if nums:
            current_num = nums[0]
            try:
                operations_dict['d'] /= current_num
                nums.popleft()
            except:
                nums.popleft()
        if nums:
            current_num = nums.popleft()
            operations_dict['m'] *= current_num
    return operations_dict



print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
