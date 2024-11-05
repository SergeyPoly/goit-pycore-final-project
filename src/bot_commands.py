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
def change_contact(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    record.edit_phone(old_phone, new_phone)
    
    return "Contact updated."
    

@input_error
def show_phone(args: list[str], book: AddressBook) -> str: 
    name = args[0]
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    return record


@show_all_error
def show_all(book: AddressBook) -> str:
    if not book:
        raise ValueError
    
    return "\n".join(f"{record}" for record in book.values())


@input_error
def add_birthday(args: list[str], book: AddressBook):
    name, birthday = args
    record: Record = book.find(name)

    if record is None:
        raise KeyError(name)
    
    record.add_birthday(birthday)
    
    return "Birthday added."


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

#для повноцінного меню необхідно розширити словник команд, а саме додати опис кожної команди
commands = {
    "hello": lambda *args: "How can I help you?",
    "add": lambda args, book: add_contact(args, book),
    "change": lambda args, book: change_contact(args, book),
    "phone": lambda args, book: show_phone(args, book),
    "all": lambda args, book: show_all(book),
    "add-birthday": lambda args, book: add_birthday(args, book),
    "show-birthday": lambda args, book: show_birthday(args, book),
    "birthdays": lambda args, book: birthdays(book),
}

exit_commands = ["close", "exit"]