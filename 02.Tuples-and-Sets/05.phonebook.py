def add_number(name, number, contacts):
    if name not in contacts.items():
        contacts[name] = 0
    contacts[name] = number
    return contacts


def print_result(name, contacts):
    if name not in contacts.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {contacts[name]}")


command = input()
contacts = {}

while not command.isdigit():
    name, number = command.split('-')
    contacts = add_number(name, number, contacts)
    command = input()

n = int(command)
for result in range(n):
    print_result(input(), contacts)