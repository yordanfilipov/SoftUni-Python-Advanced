SNAKE_SYMBOL = "S"


def read_matrix(n):
    return [list(input()) for _ in range(n)]


def in_range(value, max_value):
    return 0 <= value < max_value


def game_over(matrix, eaten_food):
    if eaten_food < 10:
        print("Game over!")
    else:
        print("You won! You fed the snake.")
    print(f"Food eaten: {eaten_food}")
    for i in range(len(matrix)):
        print(f'{"".join(matrix[i])}')
    exit()


def change_position(matrix, snake_position, mapper, eaten_food):
    while True:
        command = input()
        current_row = snake_position[0]
        current_col = snake_position[1]
        row = mapper[command][0] + snake_position[0]
        col = mapper[command][1] + snake_position[1]
        if not in_range(row, len(matrix)) \
                or not in_range(col, len(matrix)):
            matrix[current_row][current_col] = "."
            game_over(matrix, eaten_food)
        matrix[current_row][current_col] = "."
        if matrix[row][col] == "-":
            matrix[row][col] = SNAKE_SYMBOL
            snake_position = row, col
        elif matrix[row][col] == "B":
            matrix[row][col] = "."
            for r in range(len(matrix)):
                for c in range(len(matrix)):
                    if matrix[r][c] == "B":
                        snake_position = r, c
                        matrix[r][c] = SNAKE_SYMBOL
                        break
        elif matrix[row][col] == "*":
            eaten_food += 1
            matrix[row][col] = SNAKE_SYMBOL
            snake_position = row, col
        if eaten_food == 10:
            game_over(matrix, eaten_food)


def find_snake_position(matrix):
    for row_index in range(len(matrix)):
        if SNAKE_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(SNAKE_SYMBOL)
            return row_index, column_index


eaten_food = 0
mapper = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
n = int(input())
matrix = read_matrix(n)
snake_position = find_snake_position(matrix)
matrix = change_position(matrix, snake_position, mapper, eaten_food)
