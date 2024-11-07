from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from colorama import Style
from colorama import Fore

class PrettyOutput:
    def __init__(self):
        self.table = PrettyTable()
        self.table.set_style(SINGLE_BORDER)
        self.table.field_names = [Fore.GREEN + 'Commands', Fore.YELLOW + 'Description' + Fore.WHITE]
        self.table.align[Fore.GREEN + 'Commands'] = 'l'
        self.table.align[Fore.YELLOW +'Description' + Fore.WHITE] = 'l'


    def print_all_commands(self, all_commands_lists) -> str:
        matrix = []
        for commands_list in all_commands_lists:
            for key in commands_list.keys():
                comand = Fore.GREEN + key + Fore.WHITE
                description = Fore.YELLOW + commands_list[key]['description'] + Fore.WHITE 
                line = [comand, description]
                matrix.append(line)
        self.table.add_rows(matrix)
        string_table = str(self.table)
        print(string_table + Style.RESET_ALL)