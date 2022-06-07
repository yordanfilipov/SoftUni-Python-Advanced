integers = [el for el in input().split()]

reversed_integers = []

while integers:
    reversed_integers.append(integers.pop())

print(' '.join(reversed_integers))