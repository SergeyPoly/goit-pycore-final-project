from .fields import Name, Phone, Birthday, Email, Address
from .custom_errors import NotFoundError, DuplicationError


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None
        self.email: Email | None = None
        self.address: Address | None = None

    def add_phone(self, phone: str) -> None:
        if phone in map(lambda phone: phone.value, self.phones):
            raise DuplicationError("Phone already added.")

        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_email(self, email: str) -> None:
        self.email = Email(email)

    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        old_phone_obj = self.find_phone(old_phone)

        if old_phone_obj:
            new_phone_obj = Phone(new_phone)
            index = self.phones.index(old_phone_obj)
            self.phones[index] = new_phone_obj

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)

        if phone_obj:
            self.phones.remove(phone_obj)

    def find_phone(self, phone: str) -> Phone:
        searched_phone = next((p for p in self.phones if p.value == phone), None)

        if not searched_phone:
            raise NotFoundError(
                f"No such phone number: {phone} in the list for {self.name}"
            )

        return searched_phone

    def __str__(self):
        def check_data(property) -> str:
            return "no data" if property is None else property.value

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {check_data(self.birthday)}, email: {check_data(self.email)}, address: {check_data(self.address)}"
