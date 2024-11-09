from prettytable import PrettyTable, SINGLE_BORDER
from colorama import Fore, Style


class BotMenu:
    def __init__(self, all_commands: dict[str, dict[str, str]]):
        all_commands_list = [c for c in all_commands]

        table_rows = map(
            lambda command: [
                Fore.YELLOW + command + Style.RESET_ALL,
                Fore.LIGHTBLACK_EX
                + all_commands[command]["description"]
                + Style.RESET_ALL,
            ],
            all_commands_list,
        )

        command_field = Fore.GREEN + "Command" + Style.RESET_ALL
        description_field = Fore.GREEN + "Description" + Style.RESET_ALL

        self.__table = PrettyTable([command_field, description_field])
        self.__table.set_style(SINGLE_BORDER)
        self.__table.align[command_field] = "l"
        self.__table.align[description_field] = "l"
        self.__table.add_rows(table_rows)

    def __print_message(self, message: str, color: str = ""):
        print(color + f"\n{message}\n" + Style.RESET_ALL)

    def print_help_menu(self):
        string_table = str(self.__table)
        self.__print_message(string_table)

    def print_welcome(self):
        self.__print_message("Welcome to the assistant bot!", Fore.GREEN)

    def print_good_bye(self):
        self.__print_message("Good bye!", Fore.GREEN)

    def print_invalid_cmd(self):
        self.__print_message(
            f"Invalid command or no command entered. Type {Fore.YELLOW + "'help'" + Fore.RED} to see possible options",
            Fore.RED,
        )
