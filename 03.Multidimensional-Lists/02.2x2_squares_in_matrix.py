rows, cols = input().split()
rows = int(rows)
cols = int(cols)

matrix = []

counter = 0

for i in range(rows):
    elements = [el for el in input().split()]
    matrix.append(elements)

for r in range(rows - 1):
    for c in range(cols - 1):
        symbol = matrix[r][c]
        if symbol == matrix[r + 1][c]:
            if symbol == matrix[r][c + 1]:
                if symbol == matrix[r + 1][c + 1]:
                    counter += 1
print(counter)