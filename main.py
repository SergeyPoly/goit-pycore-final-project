from src import (
    parse_input,
    contact_commands,
    exit_commands,
    help_commands,
    load_data,
    save_data,
    get_autocomplete_input,
)
from src.classes import PrettyOutput 


def main():
    ADDRESSBOOK_FILENAME = "addressbook"
    book = load_data(ADDRESSBOOK_FILENAME)
    all_commands = [c for c in {**help_commands, **contact_commands, **exit_commands}]
    autocomplete_input = get_autocomplete_input(all_commands)

    # TODO: наступний вивід переробити на повноцінне меню
    print("Welcome to the assistant bot!")
    pretty_output = PrettyOutput() 
    pretty_output.print_all_commands([contact_commands, exit_commands, help_commands])

    while True:
        user_input = autocomplete_input(
            "Enter a command: ",
        )

        command, *args = parse_input(user_input)

        if command in exit_commands:
            save_data(book, ADDRESSBOOK_FILENAME)
            print("Good bye!")
            break

        if command in contact_commands:
            print(contact_commands[command]["handler"](args, book))

        else:
            # наступний вивід переобити запропонувати команду help яка буде виводити меню що і з початку
            print(
                f"Invalid command or no command entered.\nPossible options: {', '.join(all_commands)}."
            )


if __name__ == "__main__":
    main()
