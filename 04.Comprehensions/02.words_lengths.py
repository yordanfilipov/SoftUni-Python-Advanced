# names = input().split(', ')
#
# result = [f'{name} -> {len(name)}' for name in names]
# print(', '.join(result))

print(', '.join([f'{name} -> {len(name)}' for name in input().split(', ')]))