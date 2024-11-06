from src import (
    parse_input,
    commands,
    exit_commands,
    load_data,
    save_data,
    get_autocomplete_input,
)


def main():
    FILENAME = "addressbook"
    book = load_data(FILENAME)

    all_commands = [c for c in commands] + exit_commands
    autocomplete_input = get_autocomplete_input(all_commands)

    # TODO: наступний вивід переробити на повноцінне меню
    print("Welcome to the assistant bot!")

    while True:
        user_input = autocomplete_input(
            "Enter a command: ",
        )

        command, *args = parse_input(user_input)

        if command in exit_commands:
            save_data(book, FILENAME)
            # аналогічно збереження даних по нотаткам
            print("Good bye!")
            break

        if command in commands:
            print(commands[command](args, book))

        else:
            # наступний вивід переобити запропонувати команду help яка буде виводити меню що і з початку
            print(
                f"Invalid command or no command entered.\nPossible options: {', '.join(all_commands)}."
            )


if __name__ == "__main__":
    main()
