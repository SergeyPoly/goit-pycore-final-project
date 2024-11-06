from src.handlers import (
    add_contact,
    add_phone,
    add_address,
    add_email,
    change_phone,
    change_birthday,
    change_email,
    change_address,
    delete_contact,
    delete_phone,
    show_all,
    search_by_phone,
    search_by_email,
    show_phone,
    add_birthday,
    show_birthday,
    birthdays,
)

help_commands = {
    "help": {
        # add handler that will show menu or description
        "handler": lambda *args: "How can I help you?",
        "description": "shows all menu options or a specific comand description",
    },
}

exit_commands = {
    "close": {
        "description": "exit the application",
    },
    "exit": {
        "description": "exit the application",
    },
}

contact_commands = {
    "add-contact": {
        "handler": lambda args, book: add_contact(args, book),
        "description": "adds a new contact, requires 'name' and 'phone number'",
    },
    "add-phone": {
        "handler": lambda args, book: add_phone(args, book),
        "description": "adds additional phone number to the specified contact, requires 'name' and 'phone number'",
    },
    "add-birthday": {
        "handler": lambda args, book: add_birthday(args, book),
        "description": "adds birthday date to the specified contact, requires 'name' and 'birthday date'",
    },
    "add-email": {
        "handler": lambda args, book: add_email(args, book),
        "description": "adds email to the specified contact, requires 'name' and 'email'",
    },
    "add-address": {
        "handler": lambda args, book: add_address(args, book),
        "description": "adds address info to the specified contact, requires 'name' and 'address'",
    },
    "change-phone": {
        "handler": lambda args, book: change_phone(args, book),
        "description": "changes phone number for the specified contact, requires 'name', 'old phone number' and 'new phone number'",
    },
    "change-birthday": {
        "handler": lambda args, book: change_birthday(args, book),
        "description": "changes birthday date for the specified contact, requires 'name' and 'birthday date'",
    },
    "change-email": {
        "handler": lambda args, book: change_email(args, book),
        "description": "changes email for the specified contact, requires 'name' and 'email'",
    },
    "change-address": {
        "handler": lambda args, book: change_address(args, book),
        "description": "changes address info for the specified contact, requires 'name' and 'address'",
    },
    "delete-contact": {
        "handler": lambda args, book: delete_contact(args, book),
        "description": "deletes contact, requires 'name'",
    },
    "delete-phone": {
        #can't delete if one phone record remains
        "handler": lambda args, book: delete_phone(args, book),
        "description": "deletes phone number of the specified contact, requires 'name' and 'phone number'",
    },
    "show-all-contacts": {
        #add optional search by name
        "handler": lambda args, book: show_all(book),
        "description": "shows all contacts info in the address book",
    },
    "search-contacts-by-phone": {
        "handler": lambda args, book: search_by_phone(book),
        "description": "shows all contacts info in the address book",
    },
    "search-contacts-by-email": {
        "handler": lambda args, book: search_by_email(book),
        "description": "shows all contacts info in the address book",
    },
    "show-phone": {
        "handler": lambda args, book: show_phone(args, book),
        "description": "shows all phone numbers for the specified contact, requires 'name'",
    },
    "show-birthday": {
        "handler": lambda args, book: show_birthday(args, book),
        "description": "shows birthday info for the specified contact, requires 'name'",
    },
    "upcoming-birthdays": {
        "handler": lambda args, book: birthdays(book),
        "description": "shows upcoming birthdays in the next week or 'number of days' specified by the user",
    },
}
