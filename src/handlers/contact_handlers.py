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
    name, phone = args
    record: Record = book.find(name, True)

    if phone in map(lambda phone: phone.value, record.phones):
        return "Phone already added."

    record.add_phone(phone)

    return "Phone added."


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args
    record: Record = book.find(name, True)

    record.add_birthday(birthday)

    return "Birthday updated."


@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    name, email = args
    record: Record = book.find(name, True)

    record.add_email(email)

    return "Email updated."


@input_error
def add_address(args: list[str], book: AddressBook) -> str:
    name, *address = args
    record: Record = book.find(name, True)

    record.add_address(" ".join(address))

    return "Address updated."


@input_error
def change_phone(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record: Record = book.find(name, True)

    record.edit_phone(old_phone, new_phone)

    return "Phone updated."


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]
    book.delete(name)

    return "Contact removed."


@input_error
def delete_phone(args: list[str], book: AddressBook) -> str:
    name, phone = args
    record: Record = book.find(name, True)

    if len(record.phones) < 2:
        return "Unable to delete last phone number from contact."

    record.remove_phone(phone)

    return "Phone removed."


@show_all_error
def show_all(args: list[str], book: AddressBook) -> str:
    if not book:
        raise NotFoundError

    if bool(len(args)):
        search_fragment = args[0]
        found_records = [
            record
            for record in sorted(book.values(), key=lambda record: record.name.value)
            if search_fragment in record.email.value
        ]

        if not bool(len(found_records)):
            return "No contacts found."
            
        return "\n".join(f"{record}" for record in found_records)      

    return "\n".join(
        f"{record}"
        for record in sorted(book.values(), key=lambda record: record.name.value)
    )


@show_all_error
def search_by_phone(args: list[str], book: AddressBook) -> str:
    if not book:
        raise NotFoundError
    
    search_fragment = args[0]
    found_records = book.search_by_phone(search_fragment)

    if not bool(len(found_records)):
        return "No contacts found."
            
    return "\n".join(f"{record}" for record in sorted(found_records, key=lambda record: record.name.value))    


@show_all_error
def search_by_email(args: list[str], book: AddressBook) -> str:
    if not book:
        raise NotFoundError
    
    search_fragment = args[0]
    found_records = book.search_by_email(search_fragment)

    if not bool(len(found_records)):
        return "No contacts found."
            
    return "\n".join(f"{record}" for record in sorted(found_records, key=lambda record: record.name.value)) 


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)

    return record


@input_error
def show_birthday(args: list[str], book):
    name = args[0]
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)

    if record.birthday is None:
        raise NotFoundError(f"Birthday date is unknown for {name}")

    return f"Contact name: {record.name.value}, birthday: {record.birthday.value.strftime("%d.%m.%Y")}"


@show_all_error
def birthdays(args: list[str], book: AddressBook):
    if not book:
        raise NotFoundError

    days = int(args[0]) if bool(len(args)) else 7

    if days < 1:
        raise ValueError

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    if not upcoming_birthdays:
        return f"No upcoming birthdays in the next {days} days."

    return "\n".join(
        f"Contact name: {data["name"]}, birthday: {data["birthday"]}, congratulation date: {data["congratulation_date"]}"
        for data in upcoming_birthdays
    )
