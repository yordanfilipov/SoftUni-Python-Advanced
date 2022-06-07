def make_a_set(my_range):
    first_index = int(my_range.split(',')[0])
    second_index = int(my_range.split(',')[1])
    my_set = set(el for el in range(first_index, second_index + 1))
    return my_set


def intersection_set(first, second, longest):
    current_longest = first.intersection(second)
    if len(current_longest) > len(longest):
        longest = current_longest
    return longest


n = int(input())
longest = set()

for i in range(n):
    first_range, second_range = input().split('-')
    first_set = make_a_set(first_range)
    second_set = make_a_set(second_range)
    longest = intersection_set(first_set, second_set, longest)
longest = list(longest)
print(f"Longest intersection is {longest} with length {len(longest)}")