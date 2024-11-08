from src.decorators import with_input_error_handler, with_empty_check
from src.classes import Note, NoteBook
from src.types import CmdArgs
from .helpers import get_note_description


@with_input_error_handler("Enter note name and description please.")
def add_note(args: CmdArgs, notebook: NoteBook) -> str:
    name, *description_parts = args

    description = get_note_description(description_parts)

    try:
        note = notebook.find(name)
        note.edit(description)
    except:
        notebook.add_note(Note(name, description))

    return "Note added."


@with_input_error_handler("Enter note name please.")
def find_note(args: CmdArgs, notebook: NoteBook) -> str:
    (name,) = args

    note = notebook.find(name)

    return str(note)


@with_input_error_handler("Enter note name and new description please.")
def edit_note(args: CmdArgs, notebook: NoteBook) -> str:
    name, *description_parts = args

    description = get_note_description(description_parts)

    note = notebook.find(name)

    note.edit(description)

    return "Note updated."


@with_input_error_handler("Enter note name please.")
def delete_note(args: CmdArgs, notebook: NoteBook) -> str:
    (name,) = args

    notebook.delete(name)

    return "Note deleted."


@with_empty_check("notes")
def show_all(args: CmdArgs, notebook: NoteBook) -> str:
    return "\n".join(f"{note}" for note in notebook.values())
