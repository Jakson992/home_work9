my_contacts = {}
my_chat = True
while my_chat:
    user_input = input('>>> ')
    user_input = user_input.lower()
    if user_input == 'good byu' or user_input == 'close' or user_input == 'exit':
        print('Good Buy!')
        break
    elif user_input == 'hello':
        print('Can I help you?')
    elif user_input.startswith('add'):
        _, name, phone = user_input.split()
        my_contacts[name] = phone
        print(f'Contacts {name} with phone {phone} has added')
    elif user_input.startswith('change'):
        _, name, phone = user_input.split()
        if name in my_contacts:
            my_contacts[name] = phone
            print(f'Phone number for contact {name} changed')
        else:
            print(f'Contacts with {name} not found')
    elif user_input.startswith('phone'):
        _, name = user_input.split()
        if name in my_contacts:
            phone = my_contacts[name]
            print(f'Phone number for contact {name} is showed')
        else:
            print(f'Contact with name {name} is not defined')
    elif user_input == 'show all':
        if my_contacts:
            for name, phone in my_contacts.items():
                print(f'{name} : {phone}')
        else:
            print('You have not contacts')

    else:
        print("Unknown command.")
