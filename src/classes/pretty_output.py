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