from collections import UserDict
from .note import Note
from .custom_errors import NotFoundError


class NoteBook(UserDict[str, Note]):
    def add_note(self, note: Note):
        self.data[note.name.value] = note

    def find(self, name: str) -> Note:
        note = self.data.get(name)

        if not note:
            raise NotFoundError(f"Note '{name}' not found")

        return note

    def edit(self, name: str, description: str):
        note = self.find(name)

        note.edit(description)

    def delete(self, name: str):
        self.find(name)

        del self.data[name]
