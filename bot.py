phone_book = {'sasha': '0631456677', 'masha': '0928763456'}

def input_error(func):
    def wrapper(name):
        try:
            phone_number = name.split(" ")[2]
            if phone_number.isdigit():
                my_dict = {name.split(" ")[1]: name.split(" ")[2]}
                result = func(my_dict)
            else:
                result = 'In phone number only numbers allowed!'
        except IndexError:
            result = 'There must be a space between the name and the phone number!'
        return result
    return wrapper

@input_error
def add_contact(name):
    phone_book.update(name)
    return 'Saved'

@input_error
def change_contact(name):
    if phone_book.get(list(name.keys())[0]):
        phone_book.update(name)
        return 'Saved'
    else:
        return 'There is no such contact'

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
        return add_contact(command)
    elif command.split(" ")[0] == 'change':
        return change_contact(command)
    elif command.split(" ")[0] == 'phone':
        return show_phone(command)
    elif 'show all' in command:
        return show_all()
    elif command in ("good bye", "close", "exit"):
        return "Good bye!"
    else:
        return "Unknown command"

def main():
    input_var = ''
    while input_var not in ["good bye", "close", "exit"]:
        print("\nEnter the command: ")
        raw_input = input().lower()
        command = command_parser(raw_input)
        print(command)
        input_var = raw_input
    else:
        pass

if __name__ == "__main__":
    main()