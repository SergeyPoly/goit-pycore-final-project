from .fields import Name, Description


class Note:
    def __init__(self, name: str, description: str):
        self.name = Name(name)
        self.description = Description(description)

    def __str__(self):
        return str(f"{self.name}: {self.description}")

    def edit(self, description: str):
        self.description = Description(description)
