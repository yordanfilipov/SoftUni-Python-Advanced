nums = [int(x) for x in input().split(', ')]


def print_result(nums):
    ll = list(map(str, nums))
    return ', '.join(ll)


positives = [x for x in nums if x >= 0]
negatives = [x for x in nums if x < 0]
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 == 1]

print(f'Positive: {print_result(positives)}')
print(f'Negative: {print_result(negatives)}')
print(f'Even: {print_result(evens)}')
print(f'Odd: {print_result(odds)}')