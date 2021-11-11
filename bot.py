phone_book = {'sasha': '0631456677', 'masha': '0928763456'}

def input_error(func):
    def wrapper(name):
        try:
            if name.split(" ")[2].isdigit():
                my_dict = {name.split(" ")[1]: name.split(" ")[2]}
                result = func(my_dict)
            else:
                result = 'In phone number only numbers allowed!'
        except IndexError:
            result = 'There must be a space between the name and the phone number!'
        return result
    return wrapper

@input_error
def add_and_change_contact(name):
    phone_book.update(name)
    return 'Saved'

def show_all():
    contacts = ''
    for k, v in phone_book.items():
        contacts += f'{k.title()} {v}\n'
    return contacts

def show_phone(command):
    if phone_book.get(command.split(" ")[1]):
        return phone_book.get(command.split(" ")[1])
    else:
        return 'There is no such contact'

def command_parser(command):
    if command.split(" ")[0] == 'hello':
        return 'How can I help you?'
    elif command.split(" ")[0] == 'add':
        return add_and_change_contact(command)
    elif command.split(" ")[0] == 'change':
        return add_and_change_contact(command)
    elif command.split(" ")[0] == 'phone':
        return show_phone(command)
    elif 'show all' in command:
        return show_all()
    elif command in ("good bye", "close", "exit"):
        return "Good bye!"
    else:
        return "Unknown command"

def main():
    while True:
        print("\nEnter the command: ")
        command = command_parser(input().lower())
        print(command)
        if command == "Good bye!":
            break

main()