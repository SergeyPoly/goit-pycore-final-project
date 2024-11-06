from src import (
    parse_input,
    contact_commands,
    exit_commands,
    help_commands,
    load_data,
    save_data,
)


def main():
    book = load_data("addressbook")
    # аналогічно завантаження даних по нотаткам
    all_commands = ", ".join(
        [command for command in help_commands]
        + [command for command in contact_commands]
        + [command for command in exit_commands]
    )
    # наступний вивід переобити на повноцінне меню
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in exit_commands:
            save_data(book, "addressbook")
            # аналогічно збереження даних по нотаткам
            print("Good bye!")
            break

        if command in contact_commands:
            print(contact_commands[command]["handler"](args, book))

        else:
            # наступний вивід переобити запропонувати команду help яка буде виводити меню що і з початку
            print(
                f"Invalid command or no command entered.\nPossible options: {all_commands}."
            )


if __name__ == "__main__":
    main()
