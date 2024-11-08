import re
from .field import Field
from ..custom_errors import ValidationError


class Email(Field[str]):
    def __init__(self, value: str):
        if self.__is_email_valid(value):
            self.value = value

        else:
            raise ValidationError("Incorrect email format")

    def __is_email_valid(self, email: str) -> bool:
        return bool(
            re.match(
                r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
                email,
            )
        )
