def input_to_list(count):
    lines = []
    for _ in range(count):
        command = input().split()
        for el in command:
            lines.append(el)
    return lines


def print_result(names):
    for name in names:
        print(name)


n = int(input())
elements = input_to_list(n)
print_result(set(elements))