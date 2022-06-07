numbers = [int(el) for el in input().split()]
positive_nums = [el for el in numbers if el > 0]
negative_nums = [el for el in numbers if el < 0]
print(sum(negative_nums))
print(sum(positive_nums))
if abs(sum(negative_nums)) > sum(positive_nums):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")