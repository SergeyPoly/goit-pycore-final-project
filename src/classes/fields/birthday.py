import re
from datetime import datetime
from .field import Field
from ..custom_errors import ValidationError


class Birthday(Field):
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, value: str):
        if self.__is_date_valid(value):
            self.value = datetime.strptime(value, Birthday.DATE_FORMAT).date()

        else:
            raise ValidationError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(Birthday.DATE_FORMAT)

    def __is_date_valid(self, date: str) -> bool:
        date_pattern = r"^(0[1-9]|[12]\d|3[01]).(0[1-9]|1[0-2]).\d{4}$"
        return bool(re.match(date_pattern, date))
