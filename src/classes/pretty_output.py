from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from colorama import Fore, Style

class MenuOutput:
    def __init__(self):
        self.table = PrettyTable()
        self.table.set_style(SINGLE_BORDER)
        self.table.field_names = [Fore.GREEN + 'Command' + Style.RESET_ALL, Fore.GREEN + 'Description' + Style.RESET_ALL]
        self.table.align[Fore.GREEN + 'Command' + Style.RESET_ALL] = 'l'
        self.table.align[Fore.GREEN + 'Description' + Style.RESET_ALL] = 'l'


    def print_menu(self, rows) -> str:
        self.table.add_rows(rows)
        string_table = str(self.table)
        print(string_table + Style.RESET_ALL)


    def print_invalid_command_message():
        print(
                Style.BRIGHT + Fore.RED + f"Invalid command or no command entered. Type 'help' to see possible options" + Style.RESET_ALL
            )
    

    def print_error_message(error_message: str) -> str:
        return Fore.RED + Style.BRIGHT + error_message + Style.RESET_ALL