def in_range(next_row, next_col):
    return 0 <= next_row < 5 and 0 <= next_col < 5


def if_targets(matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == "x":
                return True
    print(f"Training completed! All {len(count_targets)} targets hit.")
    for el in count_targets:
        print(el)
    exit()


def find_position(matrix):
    for row_index in range(len(matrix)):
        if 'A' in matrix[row_index]:
            column_index = matrix[row_index].index('A')
            return (row_index, column_index)


def move(matrix, direction, row, col, steps):
    next_row = row + (directions[direction][0] * steps)
    next_col = col + (directions[direction][1] * steps)
    if in_range(next_row, next_col) and matrix[next_row][next_col] == ".":
        matrix[next_row][next_col] = "A"
        matrix[row][col] = "."
    return matrix


def shoot(matrix, direction, row, col):
    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]
    while in_range(next_row, next_col):
        if matrix[next_row][next_col] == "x":
            count_targets.append([next_row, next_col])
            matrix[next_row][next_col] = "."
            if if_targets(matrix):
                break
        next_row += directions[direction][0]
        next_col += directions[direction][1]
    return matrix


matrix = []
count_targets = []
count_left_targets = 0
directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}

for _ in range(5):
    matrix.append(input().split())

number_of_commands = int(input())
current_position = find_position(matrix)

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "shoot":
        direction = command[1]
        row, col = current_position
        matrix = shoot(matrix, direction, row, col)
    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        row, col = current_position
        matrix = move(matrix, direction, row, col, steps)
        current_position = find_position(matrix)

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "x":
            count_left_targets += 1

if count_targets and not count_left_targets:
    print(f"Training completed! All {len(count_targets)} targets hit.")
else:
    print(f"Training not completed! {count_left_targets} targets left.")

for el in count_targets:
    print(el)
