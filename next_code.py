my_contacts = {}


def if_say_hello():
    return 'Can I help you?'


def if_say_add(user_input):
    _, name, phone = user_input.split()
    my_contacts[name] = phone
    return f'Contact {name} with phone {phone} has been added.'


def if_say_change(user_input):
    _, name, phone = user_input.split()
    if name in my_contacts:
        my_contacts[name] = phone
        return f'Phone number for contact {name} changed.'
    else:
        return f'Contact with {name} not found.'


def if_say_phone(user_input):
    _, name = user_input.split()
    if name in my_contacts:
        return f'Phone number for contact {name} is {my_contacts[name]}.'
    else:
        return f'Contact with name {name} is not defined.'


def if_say_show_all():
    if my_contacts:
        contacts_str = ""
        for name, phone in my_contacts.items():
            contacts_str += f"{name} : {phone}\n"
        return contacts_str
    else:
        return 'You have no contacts.'


def if_say_exit():
    return 'Goodbye!'


def main():
    while True:
        user_input = input('>>> ')
        user_input = user_input.lower()
        if not user_input:
            print('Please enter a command.')
        elif user_input == 'good bye' or user_input == 'close' or user_input == 'exit':
            print(if_say_exit())
            break
        elif user_input == 'hello':
            print(if_say_hello())
        elif user_input.startswith('add'):
            print(if_say_add(user_input))
        elif user_input.startswith('change'):
            print(if_say_change(user_input))
        elif user_input.startswith('phone'):
            print(if_say_phone(user_input))
        elif user_input == 'show all':
            print(if_say_show_all())
        else:
            print('Unknown command.')


if __name__ == '__main__':
    main()
