from src.classes import Record
from src.types import CmdArgs


def format_records(records: list[Record]) -> str:
    if not len(records):
        return "No contacts found."

    sorted_records = sorted(records, key=lambda record: record.name.value)

    return "\n".join(f"{record}" for record in sorted_records)


def format_upcoming_birthdays(upcoming_birthdays: list[dict[str, str]]) -> str:
    return "\n".join(
        f"Contact name: {ub["name"]}, birthday: {ub["birthday"]}, congratulation date: {ub["congratulation_date"]}"
        for ub in upcoming_birthdays
    )


def get_note_description(description_parts: CmdArgs) -> str:
    description = " ".join(description_parts)

    if not description:
        raise ValueError("Enter note description please")

    return description
