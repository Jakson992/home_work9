my_contacts = {}


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Contact with that name not found.'
        except ValueError:
            return 'Please enter a valid command.'
        except IndexError:
            return 'Please enter both name and phone number, separated by a space.'
    return wrapper


@input_error
def hello(*args):
    return 'How can I help you?'


@input_error
def add(*args):
    _, name, phone = args[0].split()
    my_contacts[name] = phone
    return f'Contact {name} with phone {phone} has been added.'


@input_error
def change(*args):
    _, name, phone = args[0].split()
    if name in my_contacts:
        my_contacts[name] = phone
        return f'Phone number for contact {name} changed.'
    else:
        return f'Contact with {name} not found.'


@input_error
def phone(*args):
    _, name = args[0].split()
    if name in my_contacts:
        return f'Phone number for contact {name} is {my_contacts[name]}.'
    else:
        return f'Contact with name {name} is not defined.'


@input_error
def show_all(*args):
    if my_contacts:
        contacts_str = ""
        for name, phone in my_contacts.items():
            contacts_str += f"{name} : {phone}\n"
        return contacts_str
    else:
        return 'You have no contacts.'


@input_error
def exit(*args):
    return 'Goodbye!'


COMMANDS = {hello: 'hello', 
            add: 'add', 
            change: 'change',
            phone: 'phone',
            show_all: 'show all',
            exit: 'exit'}


def command_handler(text):
    for command, keywords in COMMANDS.items():
        if text.lower().startswith(keywords):
            return command, text
    return None, ''


def main():
    while True:
        user_input = input('>>> ')
        command, data = command_handler(user_input)
        if not command:
            print("Unknown command, try again.")
            continue
        print(command(data))
        if command == exit:
            break
        # user_input = user_input.lower()
        # if not user_input:
        #     print('Please enter a command.')
        # elif user_input == 'good bye' or user_input == 'close' or user_input == 'exit':
        #     print(if_say_exit())
        #     break
        # elif user_input == 'hello':
        #     print(if_say_hello())
        # elif user_input.startswith('add'):
        #     print(if_say_add(user_input))
        # elif user_input.startswith('change'):
        #     print(if_say_change(user_input))
        # elif user_input.startswith('phone'):
        #     print(if_say_phone(user_input))
        # elif user_input == 'show all':
        #     print(if_say_show_all())
        # else:
        #     print('Unknown command.')


if __name__ == '__main__':
    main()
