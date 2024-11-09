from src.output.table_output import TableItem
from .fields import Name
from abc import abstractmethod


class TableFormatted:
    name: Name

    @abstractmethod
    def format_for_table(self) -> TableItem:
        pass
