from src.handlers import notebook_handlers

notebook_commands = {
    "add-note": {
        "handler": notebook_handlers.add_note,
        "description": "Adds a new note. Requires name and description",
    },
    "edit-note": {
        "handler": notebook_handlers.edit_note,
        "description": "Edits note's description. Requires name and mew description",
    },
    "find-note": {
        "handler": notebook_handlers.find_note,
        "description": "Looks for a specific note by name",
    },
    "delete-note": {
        "handler": notebook_handlers.delete_note,
        "description": "Deletes note by name",
    },
    "show-all-notes": {
        "handler": notebook_handlers.show_all,
        "description": "Display all notes",
    },
}
