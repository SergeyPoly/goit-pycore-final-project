from src.decorators import with_empty_args_handler
from src.types import CmdArgs


@with_empty_args_handler
def parse_input(user_input: str) -> tuple[str, CmdArgs]:
    cmd, *args = user_input.split()

    return (cmd.strip().lower(), args)
