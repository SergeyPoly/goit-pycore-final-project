class Field[T]:
    def __init__(self, value: T):
        self.value = value

    def __str__(self):
        return str(self.value)
