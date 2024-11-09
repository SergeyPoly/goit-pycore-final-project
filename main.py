from src import (
    parse_input,
    contact_commands,
    exit_commands,
    help_commands,
    notebook_commands,
    load_data,
    save_data,
    get_autocomplete_input,
    BotMenu,
)


def main():
    address_book, note_book = load_data()

    common_commands = {**help_commands, **exit_commands}
    all_commands = {
        **common_commands,
        **contact_commands,
        **notebook_commands,
    }
    all_commands_list = [c for c in all_commands]

    menu = BotMenu(common_commands, contact_commands, notebook_commands)

    menu.print_welcome()
    menu.print_help_menu()

    autocomplete_input = get_autocomplete_input(all_commands_list)

    while True:
        user_input = autocomplete_input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in exit_commands:
            save_data(address_book, note_book)
            menu.print_good_bye()
            break

        if command in common_commands:
            menu.print_help_menu()

        elif command in contact_commands:
            contact_commands[command]["handler"](args, address_book)

        elif command in notebook_commands:
            notebook_commands[command]["handler"](args, note_book)

        else:
            menu.print_invalid_cmd()


if __name__ == "__main__":
    main()
