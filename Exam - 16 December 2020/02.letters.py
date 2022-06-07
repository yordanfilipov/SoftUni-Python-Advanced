word = input()
n = int(input())
matrix = []

for _ in range(n):
    command = input()
    row_list = [el for el in command]
    matrix.append(row_list)

moves = int(input())

EMPTY_POSITION = "-"
PLAYER_SYMBOL = "P"

mapper = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}


def in_range(value, max_value):
    return 0 <= value < max_value


def change_position(matrix, player, mapper, word):
    for _ in range(moves):
        command = input()
        current_row = player[0]
        current_col = player[1]
        row = mapper[command][0] + player[0]
        col = mapper[command][1] + player[1]

        if not in_range(row, len(matrix)) \
                or not in_range(col, len(matrix)):
            matrix[current_row][current_col] = "P"
            player = current_row, current_col
            if word:
                word = word[:-1]
        else:
            if not matrix[row][col] == "-":
                word += matrix[row][col]
            matrix[current_row][current_col] = "-"
            matrix[row][col] = "P"
            player = row, col
    print(word)
    for i in range(len(matrix)):
        print(f'{"".join(matrix[i])}')


def find_player_position(matrix):
    for row_index in range(len(matrix)):
        if PLAYER_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(PLAYER_SYMBOL)
            return row_index, column_index


player = find_player_position(matrix)
player_position = change_position(matrix, player, mapper, word)
