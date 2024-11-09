from .fields import Name, Description, Tag
from .table_formatted import TableFormatted
from .custom_errors import DuplicationError, NotFoundError
from src.output.table_output import TableItem


class Note(TableFormatted):
    def __init__(self, name: str, description: str):
        self.name = Name(name)
        self.description = Description(description)
        self.tags: list[Tag] = []

    def format_for_table(self) -> TableItem:
        return {
            "Name": str(self.name),
            "Description": str(self.description),
            "Tags": ", ".join(t.value for t in self.tags),
        }

    def edit(self, description: str):
        self.description = Description(description)

    def has_tag(self, tag: str) -> bool:
        for t in self.tags:
            if t.value == tag:
                return True

        return False

    def add_tag(self, tag: str):
        if self.has_tag(tag):
            raise DuplicationError(f"Note '{self.name}' already has tag '{tag}'")

        self.tags.append(Tag(tag))

    def remove_tag(self, tag: str):
        if not self.has_tag(tag):
            raise NotFoundError(f"Note '{self.name}' doesn't have tag '{tag}'")

        self.tags = [t for t in self.tags if t.value != tag]
