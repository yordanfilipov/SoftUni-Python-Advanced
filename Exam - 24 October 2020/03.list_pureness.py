def best_list_pureness(nums_list, rotations):
    best_rotation = 0
    best_sum = -99999999
    nums_list = list(nums_list)
    for rotation in range(rotations + 1):
        current_sum = 0
        for i in range(len(nums_list)):
            current_sum += nums_list[i] * i
        nums_list.insert(0, nums_list[-1])
        nums_list.pop(-1)
        if current_sum > best_sum:
            best_sum = current_sum
            best_rotation = rotation
    return f"Best pureness {best_sum} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
