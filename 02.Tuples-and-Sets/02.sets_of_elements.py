input_line = input()
first_count = int(input_line.split()[0])
second_count = int(input_line.split()[1])

first_set = set()
second_set = set()

for _ in range(first_count):
    first_set.add(int(input()))
for _ in range(second_count):
    second_set.add(int(input()))

intersected_elements = set(first_set.intersection(second_set))
for element in intersected_elements:
    print(element)