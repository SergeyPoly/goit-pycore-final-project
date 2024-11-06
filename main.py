from src import (
    parse_input,
    contact_commands,
    exit_commands,
    help_commands,
    load_data,
    save_data,
    get_autocomplete_input,
)


def main():
    ADRESBOOK_FILENAME = "addressbook"
    book = load_data(ADRESBOOK_FILENAME)
    all_commands = (
        [c for c in help_commands]
        + [c for c in contact_commands]
        + [c for c in exit_commands]
    )
    autocomplete_input = get_autocomplete_input(all_commands)

    # TODO: наступний вивід переробити на повноцінне меню
    print("Welcome to the assistant bot!")

    while True:
        user_input = autocomplete_input(
            "Enter a command: ",
        )

        command, *args = parse_input(user_input)

        if command in exit_commands:
            save_data(book, ADRESBOOK_FILENAME)
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