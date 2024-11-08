from src.decorators import with_input_error_handler, with_empty_check
from src.classes import Note, NoteBook
from src.types import CmdArgs
from .helpers import get_note_description, format_notes


@with_input_error_handler("Enter note name and description please.")
def add_note(args: CmdArgs, notebook: NoteBook) -> str:
    name, *description_parts = args

    description = get_note_description(description_parts)

    try:
        note = notebook.find_by_name(name)
        note.edit(description)
    except:
        notebook.add_note(Note(name, description))

    return "Note added."


@with_input_error_handler("Enter note name please.")
def find_note(args: CmdArgs, notebook: NoteBook) -> str:
    (name,) = args

    note = notebook.find_by_name(name)

    return str(note)


@with_input_error_handler("Enter note name and new description please.")
def edit_note(args: CmdArgs, notebook: NoteBook) -> str:
    name, *description_parts = args

    description = get_note_description(description_parts)

    note = notebook.find_by_name(name)

    note.edit(description)

    return "Note updated."


@with_input_error_handler("Enter note name please.")
def delete_note(args: CmdArgs, notebook: NoteBook) -> str:
    (name,) = args

    notebook.delete_note(name)

    return "Note deleted."


@with_input_error_handler("Enter note name and tag please.")
def add_tag(args: CmdArgs, notebook: NoteBook) -> str:
    (name, tag) = args

    notebook.add_tag(name, tag)

    return "Tag added."


@with_input_error_handler("Enter note name and tag please.")
def remove_tag(args: CmdArgs, notebook: NoteBook) -> str:
    (name, tag) = args

    notebook.remove_tag(name, tag)

    return "Tag removed."


@with_empty_check("notes")
def show_all(args: CmdArgs, notebook: NoteBook) -> str:
    return format_notes(list(notebook.values()))


@with_empty_check("notes")
@with_input_error_handler("Enter tag please.")
def show_all_by_tag(args: CmdArgs, notebook: NoteBook) -> str:
    (tag,) = args

    found_notes = notebook.find_all_by_tag(tag)

    return format_notes(found_notes)
