from .fields import Name, Description, Tag
from .custom_errors import DuplicationError, NotFoundError


class Note:
    def __init__(self, name: str, description: str):
        self.name = Name(name)
        self.description = Description(description)
        self.tags: list[Tag] = []

    def __str__(self):
        return str(
            f"Name: {self.name}, Description: {self.description}, tags: {[str(t) for t in self.tags]}"
        )

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
