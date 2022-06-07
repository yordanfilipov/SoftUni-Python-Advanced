from sys import maxsize


def sum_matrix(current_matr):
    current_sum = 0
    for row in range(3):
        for col in range(3):
            current_value = current_matr[row][col]
            current_sum += current_value
    return current_sum


def print_result(matr):
    for r in range(len(matr)):
        for c in range(len(matr)):
            print(matr[r][c], end=" ")
        print()


rows, cols = [int(el) for el in input().split()]

matrix = []

best_sum = -maxsize
current_sum = 0
best_matrix = []

for i in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        inner_matrix = []
        value = 0
        for i in range(3):
            current_row = matrix[row_index+value][col_index:col_index + 3]
            inner_matrix.append(current_row)
            value += 1
        current_sum = sum_matrix(inner_matrix)
        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = inner_matrix

print(f'Sum = {best_sum}')
print_result(best_matrix)