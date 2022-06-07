def read_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    return matrix


def is_inside_matrix(matrix, row, column):
    return row in range(len(matrix)) and column in range(len(matrix))


def placing_bombs(matrix, bombs_count):
    for i in range(bombs_count):
        bomb_place = input()[1:-1]
        row, col = bomb_place.split(", ")
        row = int(row)
        col = int(col)
        matrix[row][col] = "*"
    return matrix


def increase(matrix, row, col):
    for delta in deltas:
        next_row = row + delta[0]
        next_col = col + delta[1]

        if is_inside_matrix(matrix, next_row, next_col) \
                and matrix[next_row][next_col] != "*":
            matrix[next_row][next_col] += 1
    return matrix


def calculate_numbers(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "*":
                matrix = increase(matrix, r, c)
    return matrix


def print_result(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])


deltas = [
    (0, -1), (-1, -1), (-1, 0), (-1, +1),
    (0, +1), (+1, +1), (+1, 0), (+1, -1)
]

n = int(input())
bombs_count = int(input())
matrix = read_matrix(n)
matrix = placing_bombs(matrix, bombs_count)
matrix = calculate_numbers(matrix)
print_result(matrix)
