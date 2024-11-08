import re
from .field import Field
from ..custom_errors import ValidationError


class Phone(Field[str]):
    def __init__(self, value: str):
        if self.__is_phone_valid(value):
            self.value = value

        else:
            raise ValidationError("Incorrect phone number. Use 10 numbers")

    def __is_phone_valid(self, phone: str) -> bool:
        return bool(re.fullmatch(r"\d{10}", phone))
