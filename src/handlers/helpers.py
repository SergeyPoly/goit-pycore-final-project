from src.classes import Record, Note, UpcomingBirthday
from src.types import CmdArgs


def format_records(records: list[Record]) -> str:
    if not len(records):
        return "No contacts found."

    sorted_records = sorted(records, key=lambda record: record.name.value)

    return "\n".join(f"{record}" for record in sorted_records)


def format_notes(notes: list[Note]) -> str:
    if not len(notes):
        return "No notes found."

    sorted_notes = sorted(notes, key=lambda note: note.name.value)

    return "\n".join(f"{note}" for note in sorted_notes)


def format_upcoming_birthdays(upcoming_birthdays: list[UpcomingBirthday]) -> str:
    return "\n".join(str(ub) for ub in upcoming_birthdays)


def get_arg_from_parts(arg_parts: CmdArgs, arg_name: str) -> str:
    arg = " ".join(arg_parts)

    if not arg:
        raise ValueError(f"Enter {arg_name} please")

    return arg


def get_contact_address(address_parts: CmdArgs) -> str:
    return get_arg_from_parts(address_parts, "address")


def get_note_description(description_parts: CmdArgs) -> str:
    return get_arg_from_parts(description_parts, "note description")
