row_count = int(input())
matrix = []


def current_matrix(row, col, matrix):
    destoied_position = matrix[row][col]
    if row - 1 >= 0 and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= destoied_position
    if row - 1 >= 0 and col - 1 >= 0 and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= destoied_position
    if row - 1 >= 0 and col + 1 < len(matrix) and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= destoied_position
    if col - 1 >= 0 and matrix[row][col - 1] > 0 and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= destoied_position
    if col + 1 < len(matrix) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= destoied_position
    if row + 1 < len(matrix) and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= destoied_position
    if row + 1 < len(matrix) and col - 1 >= 0 and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= destoied_position
    if row + 1 < len(matrix) and col + 1 < len(matrix) and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= destoied_position

    matrix[row][col] = 0
    return matrix


for i in range(row_count):
    matrix.append(list(map(int, input().split(' '))))

coordinates = input().split(' ')

for i in range(len(coordinates)):
    current_coordinates = [int(i) for i in coordinates[i].split(',')]
    row = int(current_coordinates[0])
    col = int(current_coordinates[1])
    matrix = current_matrix(row, col, matrix)

allive_cells = 0
sum_cells = 0
for row in range(row_count):
    for col in range(row_count):
        if matrix[row][col] > 0:
            allive_cells += 1
            sum_cells += matrix[row][col]

print(f'Alive cells: {allive_cells}')
print(f'Sum: {sum_cells}')
[print(' '.join(map(str, row))) for row in matrix]
