from math import floor

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

PLAYER_SYMBOL = "P"
mapper = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
points = 0
path = []


def in_range(value, max_value):
    return 0 <= value < max_value


def game_over(path, points):
    print(f"Game over! You've collected {points} coins.")
    print("Your path:")
    if path:
        for i in range(len(path)):
            print(path[i])
    exit()


def win_game(path, points):
    print(f"You won! You've collected {points} coins.")
    print("Your path:")
    for i in range(len(path)):
        print(path[i])
    exit()


def change_position(matrix, player, mapper, path, points):
    while True:
        if points >= 100:
            win_game(path, points)
        command = input()
        if command not in mapper:
            continue
        row = mapper[command][0] + player[0]
        col = mapper[command][1] + player[1]

        if not in_range(row, len(matrix)) \
                or not in_range(col, len(matrix)) or matrix[row][col] == "X":
            points = floor(points / 2)
            game_over(path, points)

        points += int(matrix[row][col])
        path.append([row, col])
        player = row, col


def find_player_position(matrix):
    for row_index in range(len(matrix)):
        if PLAYER_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(PLAYER_SYMBOL)
            return row_index, column_index


player = find_player_position(matrix)
player_position = change_position(matrix, player, mapper, path, points)
