from prompt_toolkit import prompt
from prompt_toolkit.filters import completion_is_selected
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.completion import WordCompleter
from typing import Callable


def get_autocomplete_input(
    commands: list[str],
) -> Callable[[str], str]:
    bindings = KeyBindings()

    @bindings.add("enter", filter=completion_is_selected)
    def _(event):
        # Enter має лише закривати меню замість того щоб повертати input
        event.current_buffer.complete_state = None
        event.app.current_buffer.complete_state = None

    commands_completer = WordCompleter(commands, sentence=True)

    def autocomplete_input(message: str):
        return prompt(message, completer=commands_completer, key_bindings=bindings)

    return autocomplete_input
