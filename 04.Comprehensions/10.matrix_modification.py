def print_matrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            print(matrix[r][c], end=" ")
        print()


def is_valid_coords(matrix, row_index, col_index):
    if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix):
        return True
    print("Invalid coordinates")
    return False


n = int(input())
matrix = []

for i in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

command = input()

while not command == "END":
    action, row_index, col_index, value = command.split()
    row_index = int(row_index)
    col_index = int(col_index)
    value = int(value)
    if is_valid_coords(matrix, row_index, col_index):
        if action == "Add":
            matrix[row_index][col_index] += value
        elif action == "Subtract":
            matrix[row_index][col_index] -= value
    command = input()

print_matrix(matrix)