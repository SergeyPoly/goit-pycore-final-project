from datetime import datetime
import re
from .custom_errors import ValidationError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
		pass


class Phone(Field):
    def __init__(self, value: str):
        if self.is_phone_valid(value):
                self.value = value

        else:
            raise ValidationError("Incorrect phone number. Use 10 numbers")
        
    def is_phone_valid(self, phone: str) -> bool:
        return bool(re.fullmatch(r"\d{10}", phone))
    

class Birthday(Field):
    def __init__(self, value: str):
        if self.is_date_valid(value):
                self.value = datetime.strptime(value, "%d.%m.%Y").date()

        else:
            raise ValidationError("Invalid date format. Use DD.MM.YYYY")
        
    def is_date_valid (self, date: str) -> bool:
        date_pattern = r"^(0[1-9]|[12]\d|3[01]).(0[1-9]|1[0-2]).\d{4}$"
        return re.match(date_pattern, date)
    

class Email(Field):
    def __init__(self, value: str):
        if self.is_email_valid(value):
                self.value = value

        else:
            raise ValidationError("Incorrect email format")
        
    def is_email_valid(self, email: str) -> bool:
        return bool(re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email))
    

class Address(Field):
        #TODO add custom validation?
		pass