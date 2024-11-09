from .table_formatted import TableFormatted
from .fields import Name
from src.output.table_output import TableItem


class UpcomingBirthday(TableFormatted):
    def __init__(self, name: str, birthday: str, congratulation_date: str):
        self.name = Name(name)
        self.birthday = birthday
        self.congratulation_date = congratulation_date

    def format_for_table(self) -> TableItem:
        return {
            "Contact name": str(self.name),
            "Birthday": self.birthday,
            "Congratulation date": self.congratulation_date,
        }
