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


class BotMenu:
    def __init__(self, all_commands: dict[str, dict[str, str]]):
        commands_table_data = [
            {"Command": command, "Description": command_data["description"]}
            for command, command_data in all_commands.items()
        ]

        self.__table = create_table(commands_table_data, self.__format_value)

    def __format_value(self, index: int, field: str) -> str:
        color = COMMAND_COLOR if index == 0 else COMMON_TEXT_COLOR
        return apply_color(field, color)

    def print_help_menu(self):
        print_table(self.__table, "Bot menu:")

    def print_welcome(self):
        print_success_message("Welcome to the assistant bot!")

    def print_good_bye(self):
        print_common_message("Good bye!")

    def print_invalid_cmd(self):
        print_error_message(
            f"Invalid command or no command entered. Type {COMMAND_COLOR + "'help'" + ERROR_COLOR} to see possible options",
        )
