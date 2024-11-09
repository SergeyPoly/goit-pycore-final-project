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

    def print_help_menu(self):
        string_table = str(self.__table)
        print(string_table + Style.RESET_ALL)

    def print_welcome(self):
        print(Fore.GREEN + "\nWelcome to the assistant bot!\n" + Style.RESET_ALL)
