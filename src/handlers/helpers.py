from src.classes import Record, Note, UpcomingBirthday, TableFormatted
from src.types import CmdArgs
from src.output.pretty_output import print_common_message
from src.output.table_output import print_table_data
from typing import Sequence


def print_single_item(item: TableFormatted):
    print_table_data([item.format_for_table()])


def print_table_formatted_items_list(
    items: Sequence[TableFormatted], type: str, empty_message=""
):
    if not len(items):
        print_common_message(empty_message or f"No {type} found.")
        return

    sorted_items = sorted(items, key=lambda item: item.name.value)
    notes_for_table = [
        {"#": str(index + 1), **item.format_for_table()}
        for index, item in enumerate(sorted_items)
    ]

    print_table_data(notes_for_table, title=f"{type.capitalize()}:")


def print_notes_list(notes: list[Note]):
    print_table_formatted_items_list(notes, "notes")


def print_contacts_list(contacts: list[Record]):
    print_table_formatted_items_list(contacts, "contacts")


def print_upcoming_birthdays(upcoming_birthdays: list[UpcomingBirthday], days: int):
    print_table_formatted_items_list(
        upcoming_birthdays,
        "upcoming birthdays",
        f"No upcoming birthdays in the next {days} days.",
    )


def get_arg_from_parts(arg_parts: CmdArgs, arg_name: str) -> str:
    arg = " ".join(arg_parts)

    if not arg:
        raise ValueError(f"Enter {arg_name} please")

    return arg


def get_contact_address(address_parts: CmdArgs) -> str:
    return get_arg_from_parts(address_parts, "address")


def get_note_description(description_parts: CmdArgs) -> str:
    return get_arg_from_parts(description_parts, "note description")


def print_contact_phones(record: Record):
    if record.phones:
        print_table_data([record.format_phones_for_table()])
    else:
        print_common_message(f"Contact {record.name} has no phones yet")


def print_contact_birthday(record: Record):
    if record.birthday:
        print_table_data([record.format_birthday_for_table()])
    else:
        print_common_message(f"Contact {record.name} has no birthday date set")
