n = int(input())
matrix = []

for row in range(n):
    current_row = [int(x) for x in input().split(', ')]
    matrix.append(current_row)

first_diagonal = []
second_diagonal = []

for index in range(n):
    current_num = matrix[index][index]
    first_diagonal.append(current_num)

first_diagonal_sum = sum(first_diagonal)

row = 0
for col in range(n - 1, -1, -1):
    current_num = matrix[row][col]
    second_diagonal.append(current_num)
    row += 1

second_diagonal_sum = sum(second_diagonal)

print(f'First diagonal: {", ".join(list(map(str, first_diagonal)))}. Sum: {first_diagonal_sum}')
print(f'Second diagonal: {", ".join(list(map(str, second_diagonal)))}. Sum: {second_diagonal_sum}')