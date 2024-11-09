from colorama import Fore, Style

ERROR_COLOR = Fore.RED
COMMAND_COLOR = Fore.YELLOW
TITLE_COLOR = Fore.GREEN
COMMON_TEXT_COLOR = Fore.LIGHTBLACK_EX


def apply_color(value: str, color: str) -> str:
    return color + value + Style.RESET_ALL


def get_line_break(apply_break: bool) -> str:
    return apply_break and "\n" or ""


def print_message(
    message: str,
    color: str = "",
    with_start_line_break=True,
    with_end_line_break=True,
):
    formatted_message = apply_color(
        f"{get_line_break(with_start_line_break)}{message}{get_line_break(with_end_line_break)}",
        color,
    )
    print(formatted_message)


def print_common_message(message: str):
    print_message(message, COMMON_TEXT_COLOR)


def print_error_message(message: str):
    print_message(message, ERROR_COLOR)


def print_success_message(message: str, with_end_line_break=True):
    print_message(message, TITLE_COLOR, True, with_end_line_break)
