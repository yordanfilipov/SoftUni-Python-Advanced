rows, cols = [int(x) for x in input().split()]

# for r in range(rows):
#     first_last_letter = chr(97 + r)
#     for c in range(cols):
#         mid_letter = chr(r + 97 + c)
#         element = first_last_letter + mid_letter + first_last_letter
#         print(f"{element}", end=" ")
#     print()


result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num+cols)]for num in range(97, 97+rows)]

print(*[' '.join(iterable) for iterable in result], sep='\n')
