from src.decorators import input_error, show_all_error
from src.classes import Record, AddressBook, NotFoundError

@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name, phone = args
    record: Record = book.find(name)

    if record:
        record.add_phone(phone)
    
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
    
    return "Contact added."


@input_error
def add_phone(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    record.add_birthday(birthday)
    
    return "Birthday added."


@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def add_address(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def change_phone(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    record.edit_phone(old_phone, new_phone)
    
    return "Contact updated."


@input_error
def change_birthday(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def change_email(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def change_address(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    pass


@input_error
def delete_phone(args: list[str], book: AddressBook) -> str:
    pass


@show_all_error
def show_all(book: AddressBook) -> str:
    if not book:
        raise ValueError
    
    return "\n".join(f"{record}" for record in book.values())


@show_all_error
def search_by_phone(book: AddressBook) -> str:
    pass


@show_all_error
def search_by_email(book: AddressBook) -> str:
    pass


@input_error
def show_phone(args: list[str], book: AddressBook) -> str: 
    name = args[0]
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    return record


@input_error
def show_birthday(args, book):
    name = args[0]
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    if record.birthday is None:
        raise NotFoundError(f"Birthday date is unknown for {name}")
    
    return f"Contact name: {record.name.value}, birthday: {record.birthday.value.strftime("%d.%m.%Y")}"


@show_all_error
#функцію і метод потрібно доробити із врахуванням вхідного аргументу кількості днів, по замовченню нехай буде 7
def birthdays(book: AddressBook):
    if not book:
        raise ValueError
    
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "No upcoming birthdays in the next 7 days."

    return "\n".join(f"Contact name: {data["name"]}, birthday: {data["birthday"]}, congratulation date: {data["congratulation_date"]}" for data in upcoming_birthdays)