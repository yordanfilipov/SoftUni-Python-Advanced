queries = int(input())

PUSH_COMMAND = "1"
DELETE_COMMAND = "2"
MAXIMUM_COMMAND = "3"
MINIMUM_COMMAND = "4"

stack = []

for i in range(queries):
    command = input()

    if command.startswith(PUSH_COMMAND):
        element = int(command.split()[1])
        stack.append(element)
    elif command == DELETE_COMMAND:
        if stack:
            stack.pop()
    elif command == MAXIMUM_COMMAND:
        if stack:
            print(max(stack))
    elif command == MINIMUM_COMMAND:
        if stack:
            print(min(stack))

new_stack = []
while stack:
    new_stack.append(stack.pop())
print(*new_stack, sep=", ")