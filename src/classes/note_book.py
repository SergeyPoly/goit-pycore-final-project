from collections import UserDict
from .note import Note
from .custom_errors import NotFoundError


class NoteBook(UserDict[str, Note]):
    def add_note(self, note: Note):
        self.data[note.name.value] = note

    def edit_note(self, name: str, description: str):
        note = self.find_by_name(name)

        note.edit(description)

    def delete_note(self, name: str):
        self.find_by_name(name)

        del self.data[name]

    def add_tag(self, name: str, tag: str):
        note = self.find_by_name(name)

        note.add_tag(tag)

    def remove_tag(self, name: str, tag: str):
        note = self.find_by_name(name)

        note.remove_tag(tag)

    def find_by_name(self, name: str) -> Note:
        note = self.data.get(name)

        if not note:
            raise NotFoundError(f"Note '{name}' not found")

        return note

    def find_all_by_tag(self, tag: str) -> list[Note]:
        notes = [note for note in self.data.values() if note.has_tag(tag)]

        return notes
