from src.decorators import with_input_error_handler, with_empty_check
from src.classes import Record, AddressBook, NotFoundError
from src.types import CmdArgs
from .helpers import format_records, format_upcoming_birthdays


@with_input_error_handler("Enter contact name and phone please.")
def add_contact(args: CmdArgs, book: AddressBook) -> str:
    name, phone = args

    try:
        record = book.find(name)
        record.add_phone(phone)
    except:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)

    return "Contact added."


@with_input_error_handler("Enter contact name and phone please.")
def add_phone(args: CmdArgs, book: AddressBook) -> str:
    name, phone = args

    record = book.find(name)
    record.add_phone(phone)

    return "Phone added."


@with_input_error_handler("Enter contact name and birthday date.")
def add_birthday(args: CmdArgs, book: AddressBook) -> str:
    name, birthday = args

    record = book.find(name)
    record.add_birthday(birthday)

    return "Birthday updated."


@with_input_error_handler("Enter contact name and email.")
def add_email(args: CmdArgs, book: AddressBook) -> str:
    name, email = args

    record = book.find(name)
    record.add_email(email)

    return "Email updated."


@with_input_error_handler("Enter contact name and address.")
def add_address(args: CmdArgs, book: AddressBook) -> str:
    name, *address_parts = args

    record = book.find(name)
    record.add_address(" ".join(address_parts))

    return "Address updated."


@with_input_error_handler("Enter contact name, old phone and new phone please.")
def change_phone(args: CmdArgs, book: AddressBook) -> str:
    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return "Phone updated."


@with_input_error_handler("Enter contact name please.")
def delete_contact(args: CmdArgs, book: AddressBook) -> str:
    (name,) = args

    book.delete(name)

    return "Contact removed."


@with_input_error_handler("Enter contact name and phone please.")
def delete_phone(args: CmdArgs, book: AddressBook) -> str:
    name, phone = args

    record = book.find(name)

    if len(record.phones) < 2:
        return "Unable to delete last phone number from contact."

    record.remove_phone(phone)

    return "Phone removed."


@with_input_error_handler("Enter contact name please.")
def show_contact(args: CmdArgs, book: AddressBook) -> str:
    (name,) = args

    contact = book.find(name)

    return str(contact)


@with_empty_check("contacts")
def show_all(args: CmdArgs, book: AddressBook) -> str:
    return format_records(list(book.values()))


@with_empty_check("contacts")
@with_input_error_handler("Enter search condition please.")
def search_by_phone(args: CmdArgs, book: AddressBook) -> str:
    (search_fragment,) = args

    found_records = book.search_by_phone(search_fragment)

    return format_records(found_records)


@with_empty_check("contacts")
@with_input_error_handler("Enter search condition please.")
def search_by_email(args: CmdArgs, book: AddressBook) -> str:
    (search_fragment,) = args

    found_records = book.search_by_email(search_fragment)

    return format_records(found_records)


@with_input_error_handler("Enter contact name please.")
def show_phone(args: CmdArgs, book: AddressBook) -> str:
    (name,) = args

    record = book.find(name)

    if not record.phones:
        f"Contact {record.name} has no phones yet"

    return f"Contact name: {record.name}, phones: {'; '.join(p.value for p in record.phones)}"


@with_input_error_handler("Enter contact name please.")
def show_birthday(args: CmdArgs, book: AddressBook) -> str:
    (name,) = args

    record = book.find(name)

    if not record.birthday:
        raise NotFoundError(f"Birthday date is unknown for {name}")

    return f"Contact name: {record.name}, birthday: {record.birthday}"


@with_empty_check("contacts")
@with_input_error_handler()
def birthdays(args: CmdArgs, book: AddressBook) -> str:
    # check the number of upcoming days specified by the user, if the user has not entered anything, the app defaults to 7
    days = int(args[0]) if len(args) else 7

    if days < 1:
        raise ValueError("Enter a positive integer please, min value 1.")

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    if not upcoming_birthdays:
        return f"No upcoming birthdays in the next {days} days."

    return format_upcoming_birthdays(upcoming_birthdays)
