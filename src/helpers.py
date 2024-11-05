from src.decorators import parse_command_error

@parse_command_error
def parse_input(user_input: str) -> list:
    cmd, *args = user_input.split()

    return cmd.strip().lower() , *args