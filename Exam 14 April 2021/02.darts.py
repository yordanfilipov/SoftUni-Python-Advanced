PLAYER_ONE_POINTS = 501
PLAYER_TWO_POINTS = 501


def read_matrix():
    matr = []
    for row_index in range(7):
        row = [x for x in input().split(' ')]
        matr.append(row)
    return matr


def change_players(current_player, player_one, player_two):
    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one
    return current_player


def calculate_points(row, col, matrix):
    points = 0
    if 0 <= row < 7 and 0 <= col < 7:
        current_position = matrix[row][col]
        if current_position == "B":
            points = 501
        elif current_position == "T":
            points = int(matrix[row][0]) + int(matrix[row][6]) + \
                     int(matrix[0][col]) + int(matrix[6][col])
            points *= 3
        elif current_position == "D":
            points = int(matrix[row][0]) + int(matrix[row][6]) + \
                     int(matrix[0][col]) + int(matrix[6][col])
            points *= 2
        else:
            points = int(matrix[row][col])
        return points
    return points


def throw(player_one, player_two, matrix, PLAYER_ONE_POINTS, PLAYER_TWO_POINTS):
    current_player = player_one
    player_one_throws = 0
    player_two_throws = 0
    while True:

        command = input()[1:-1]
        row, col = command.split(", ")
        row = int(row)
        col = int(col)
        current_points = calculate_points(row, col, matrix)
        if current_player == player_one:
            player_one_throws += 1
            PLAYER_ONE_POINTS -= current_points
            if PLAYER_ONE_POINTS <= 0:
                print(f"{player_one} won the game with {player_one_throws} throws!")
                exit()
        else:
            player_two_throws += 1
            PLAYER_TWO_POINTS -= current_points
            if PLAYER_TWO_POINTS <= 0:
                print(f"{player_two} won the game with {player_two_throws} throws!")
                exit()

        current_player = change_players(current_player, player_one, player_two)


player_one, player_two = [el for el in input().split(', ')]
matrix = read_matrix()
throw(player_one, player_two, matrix, PLAYER_ONE_POINTS, PLAYER_TWO_POINTS)
