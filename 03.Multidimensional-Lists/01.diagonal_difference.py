def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [int(x) for x in input().split(' ')]
            matrix.append(row)

        return matrix


def get_sum_of_primary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def get_sum_of_secondary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    return diagonal_sum


def print_sum(matrix):
    both_diagonals_sum = get_sum_of_primary_diagonal(matrix) - get_sum_of_secondary_diagonal(matrix)
    print(abs(both_diagonals_sum))


matrix = read_matrix()
print_sum(matrix)