from .fields import Name, Phone, Birthday, Email, Address, Field
from .table_formatted import TableFormatted
from .custom_errors import NotFoundError, DuplicationError
from src.output.table_output import TableItem


class Record(TableFormatted):
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

    def __get_phones_str(self) -> str:
        return ", ".join(p.value for p in self.phones)

    def __get_str_value(self, value: Field | None):
        return value and str(value) or ""

    def format_for_table(self) -> TableItem:
        return {
            "Contact name": str(self.name),
            "Phones": self.__get_phones_str(),
            "Birthday": self.__get_str_value(self.birthday),
            "Email": self.__get_str_value(self.email),
            "Address": self.__get_str_value(self.address),
        }

    def format_birthday_for_table(self) -> TableItem:
        return {
            "Contact name": str(self.name),
            "Birthday": self.__get_str_value(self.birthday),
        }

    def format_phones_for_table(self) -> TableItem:
        return {
            "Contact name": str(self.name),
            "Phones": self.__get_phones_str(),
        }
