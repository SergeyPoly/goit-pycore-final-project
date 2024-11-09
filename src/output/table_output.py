from prettytable import PrettyTable, SINGLE_BORDER
from src.output.pretty_output import (
    print_message,
    print_success_message,
    apply_color,
    TITLE_COLOR,
    COMMON_TEXT_COLOR,
)
from typing import Callable

type TableItem = dict[str, str]
type TableData = list[TableItem]
type FormatValueFn = Callable[[int, str], str]


def get_field_name(field: str) -> str:
    return apply_color(field, TITLE_COLOR)


def get_field_value(field: str) -> str:
    return apply_color(field, COMMON_TEXT_COLOR)


def create_table(
    table_data: TableData, format_value_fn: FormatValueFn | None = None
) -> PrettyTable:
    data_keys = table_data[0].keys()
    field_names = [get_field_name(field) for field in data_keys]

    table = PrettyTable(field_names)
    table.set_style(SINGLE_BORDER)
    for field in field_names:
        table.align[field] = "l"

    table_rows: list[list[str]] = []
    for table_item in table_data:
        row: list[str] = []
        for index, key in enumerate(data_keys):
            field_value = table_item[key]

            if format_value_fn:
                formatted_value = format_value_fn(index, field_value)
            else:
                formatted_value = get_field_value(table_item[key])

            row.append(formatted_value)

        table_rows.append(row)

    table.add_rows(table_rows)

    return table


def print_table(table: PrettyTable, title: str | None = None):
    if title:
        print_success_message(title, with_end_line_break=False)

    print_message(str(table), with_start_line_break=bool(not title))


def print_table_data(
    table_data: TableData,
    title: str | None = None,
    format_value_fn: FormatValueFn | None = None,
):
    table = create_table(table_data, format_value_fn)
    print_table(table, title)
