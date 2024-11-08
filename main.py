from colorama import Fore, Style
from src import (
    parse_input,
    contact_commands,
    exit_commands,
    help_commands,
    load_data,
    save_data,
    get_autocomplete_input,
)
from src.classes import MenuOutput


def main():
    ADDRESSBOOK_FILENAME = "addressbook"
    book = load_data(ADDRESSBOOK_FILENAME)
    all_commands = {**help_commands, **contact_commands, **exit_commands}
    all_commands_list = [c for c in all_commands]
    autocomplete_input = get_autocomplete_input(all_commands_list)
    print(Fore.GREEN + "\nWelcome to the assistant bot!\n" + Style.RESET_ALL)
    table_rows = map(
        lambda command: [
            Fore.YELLOW + command + Style.RESET_ALL,
            Fore.YELLOW + all_commands[command]["description"] + Style.RESET_ALL,
        ],
        all_commands_list,
    )
    menu = MenuOutput()
    menu.print_menu(table_rows)

    while True:
        user_input = autocomplete_input(
            "Enter a command: ",
        )

        command, *args = parse_input(user_input)

        if command in exit_commands:
            save_data(book, ADDRESSBOOK_FILENAME)
            print("Good bye!")
            break

        if command in help_commands:
            menu.print_menu(table_rows)

        elif command in contact_commands:
            print(contact_commands[command]["handler"](args, book))

        else:
            print(
                f"Invalid command or no command entered. Type 'help' to see possible options"
            )


if __name__ == "__main__":
    main()
