from prettytable import PrettyTable
from src.output.pretty_output import (
    print_success_message,
    print_common_message,
    print_error_message,
    apply_color,
    COMMAND_COLOR,
    ERROR_COLOR,
    COMMON_TEXT_COLOR,
)
from src.output.table_output import create_table, print_table

type Commands = dict[str, dict[str, str]]


class BotMenu:
    def __init__(
        self,
        common_commands: Commands,
        contacts_commands: Commands,
        notes_commands: Commands,
    ):
        self.__common_commands_table = self.__create_table(common_commands)
        self.__contacts_commands_table = self.__create_table(contacts_commands)
        self.__notes_commands_table = self.__create_table(notes_commands)

    def __create_table(self, commands: Commands) -> PrettyTable:
        commands_table_data = [
            {"Command": command, "Description": command_data["description"]}
            for command, command_data in commands.items()
        ]

        return create_table(commands_table_data, self.__format_value)

    def __format_value(self, index: int, field: str) -> str:
        color = COMMAND_COLOR if index == 0 else COMMON_TEXT_COLOR
        return apply_color(field, color)

    def __print_table(
        self, table: PrettyTable, table_name: str, with_title_start_line_break=False
    ):
        print_table(
            table,
            f"{table_name} commands:",
            with_title_start_line_break=with_title_start_line_break,
        )

    def print_help_menu(self):
        self.__print_table(
            self.__common_commands_table, "Common", with_title_start_line_break=True
        )
        self.__print_table(self.__contacts_commands_table, "Contacts")
        self.__print_table(self.__notes_commands_table, "Notes")

    def print_welcome(self):
        print_success_message(
            "Welcome to the assistant bot!", with_end_line_break=False
        )

    def print_good_bye(self):
        print_common_message("Good bye!")

    def print_invalid_cmd(self):
        print_error_message(
            f"Invalid command or no command entered. Type {COMMAND_COLOR + "'help'" + ERROR_COLOR} to see possible options",
        )
