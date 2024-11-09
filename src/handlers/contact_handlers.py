from src.decorators import with_input_error_handler, with_empty_check
from src.classes import Record, AddressBook, OperationForbiddenError
from src.types import CmdArgs
from src.output.pretty_output import print_success_message
from .helpers import (
    get_contact_address,
    print_contacts_list,
    print_single_item,
    print_upcoming_birthdays,
    print_contact_birthday,
    print_contact_phones,
)


@with_input_error_handler("Enter contact name and phone please.")
def add_contact(args: CmdArgs, book: AddressBook):
    name, phone = args

    try:
        record = book.find(name)
        record.add_phone(phone)
    except:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)

    print_success_message("Contact added.")


@with_input_error_handler("Enter contact name and phone please.")
def add_phone(args: CmdArgs, book: AddressBook):
    name, phone = args

    record = book.find(name)
    record.add_phone(phone)

    print_success_message("Phone added.")


@with_input_error_handler("Enter contact name and birthday date.")
def add_birthday(args: CmdArgs, book: AddressBook):
    name, birthday = args

    record = book.find(name)
    record.add_birthday(birthday)

    print_success_message("Birthday updated.")


@with_input_error_handler("Enter contact name and email.")
def add_email(args: CmdArgs, book: AddressBook):
    name, email = args

    record = book.find(name)
    record.add_email(email)

    print_success_message("Email updated.")


@with_input_error_handler("Enter contact name and address.")
def add_address(args: CmdArgs, book: AddressBook):
    name, *address_parts = args

    address = get_contact_address(address_parts)

    record = book.find(name)
    record.add_address(address)

    print_success_message("Address updated.")


@with_input_error_handler("Enter contact name, old phone and new phone please.")
def change_phone(args: CmdArgs, book: AddressBook):
    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    print_success_message("Phone updated.")


@with_input_error_handler("Enter contact name please.")
def delete_contact(args: CmdArgs, book: AddressBook):
    (name,) = args

    book.delete(name)

    print_success_message("Contact removed.")


@with_input_error_handler("Enter contact name and phone please.")
def delete_phone(args: CmdArgs, book: AddressBook):
    name, phone = args

    record = book.find(name)

    if len(record.phones) < 2:
        raise OperationForbiddenError(
            "Unable to delete last phone number from contact."
        )

    record.remove_phone(phone)

    print_success_message("Phone removed.")


@with_input_error_handler("Enter contact name please.")
def show_contact(args: CmdArgs, book: AddressBook):
    (name,) = args

    contact = book.find(name)

    print_single_item(contact)


@with_empty_check("contacts")
def show_all(args: CmdArgs, book: AddressBook):
    if len(args):
        search_fragment = args[0]

        print_contacts_list(book.search_by_name(search_fragment))
    else:
        print_contacts_list(list(book.values()))


@with_empty_check("contacts")
@with_input_error_handler("Enter search condition please.")
def search_by_phone(args: CmdArgs, book: AddressBook):
    (search_fragment,) = args

    found_records = book.search_by_phone(search_fragment)

    print_contacts_list(found_records)


@with_empty_check("contacts")
@with_input_error_handler("Enter search condition please.")
def search_by_email(args: CmdArgs, book: AddressBook):
    (search_fragment,) = args

    found_records = book.search_by_email(search_fragment)

    print_contacts_list(found_records)


@with_input_error_handler("Enter contact name please.")
def show_phone(args: CmdArgs, book: AddressBook):
    (name,) = args

    record = book.find(name)

    print_contact_phones(record)


@with_input_error_handler("Enter contact name please.")
def show_birthday(args: CmdArgs, book: AddressBook):
    (name,) = args

    record = book.find(name)

    print_contact_birthday(record)


@with_empty_check("contacts")
@with_input_error_handler()
def birthdays(args: CmdArgs, book: AddressBook):
    # check the number of upcoming days specified by the user, if the user has not entered anything, the app defaults to 7
    days = int(args[0]) if len(args) else 7

    if days < 1:
        raise ValueError("Enter a positive integer please, min value 1.")

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    print_upcoming_birthdays(upcoming_birthdays, days)
