from .fields import Name, Phone, Birthday
from .custom_errors import  NotFoundError

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)

        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        old_phone_obj = self.find_phone(old_phone)

        if old_phone_obj:
            new_phone_obj = Phone(new_phone)
            index = self.phones.index(old_phone_obj)
            self.phones[index] = new_phone_obj
            
    def find_phone(self, phone: str) -> Phone:
        searched_phone = next((p for p in self.phones if p.value == phone), None)

        if not searched_phone:
            raise NotFoundError(f"No such phone number: {phone} in the list for {self.name}")

        return searched_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"