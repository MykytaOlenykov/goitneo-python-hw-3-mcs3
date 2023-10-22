from classes import AddressBook
from controllers import ContactsCtrl
from utils import parse_input


def main() -> None:
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(">>> Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(ContactsCtrl.show_all(book))
        elif command == "add":
            print(ContactsCtrl.add_contact(args, book))
        elif command == "change":
            print(ContactsCtrl.change_contact(args, book))
        elif command == "delete":
            print(ContactsCtrl.delete_contact(args, book))
        elif command == "phone":
            print(ContactsCtrl.show_phone(args, book))
        elif command == "remove-phone":
            print(ContactsCtrl.remove_phone(args, book))
        elif command == "birthdays":
            print(ContactsCtrl.birthdays(book))
        elif command == "add-birthday":
            print(ContactsCtrl.add_birthday(args, book))
        elif command == "show-birthday":
            print(ContactsCtrl.show_birthday(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
