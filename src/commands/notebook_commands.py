from src.handlers import notebook_handlers

notebook_commands = {
    "add-note": {
        "handler": notebook_handlers.add_note,
        "description": "Adds a new note. Requires name and description",
    },
    "edit-note": {
        "handler": notebook_handlers.edit_note,
        "description": "Edits note's description. Requires name and new description",
    },
    "find-note": {
        "handler": notebook_handlers.find_note,
        "description": "Looks for a specific note by name",
    },
    "delete-note": {
        "handler": notebook_handlers.delete_note,
        "description": "Deletes note by name",
    },
    "add-note-tag": {
        "handler": notebook_handlers.add_tag,
        "description": "Adds a tag to a note",
    },
    "remove-note-tag": {
        "handler": notebook_handlers.remove_tag,
        "description": "Removes a tag from a note",
    },
    "show-all-notes": {
        "handler": notebook_handlers.show_all,
        "description": "Display all notes",
    },
    "show-notes-by-tag": {
        "handler": notebook_handlers.show_all_by_tag,
        "description": "Display all notes that have the tag",
    },
}
