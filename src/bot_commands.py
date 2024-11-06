from .handlers import contact_handlers

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
        "handler": contact_handlers.add_contact,
        "description": "adds a new contact, requires 'name' and 'phone number'",
    },
    "add-phone": {
        "handler": contact_handlers.add_phone,
        "description": "adds additional phone number to the specified contact, requires 'name' and 'phone number'",
    },
    "add-birthday": {
        "handler": contact_handlers.add_birthday,
        "description": "adds birthday date to the specified contact, requires 'name' and 'birthday date'",
    },
    "add-email": {
        "handler": contact_handlers.add_email,
        "description": "adds email to the specified contact, requires 'name' and 'email'",
    },
    "add-address": {
        "handler": contact_handlers.add_address,
        "description": "adds address info to the specified contact, requires 'name' and 'address'",
    },
    "change-phone": {
        "handler": contact_handlers.change_phone,
        "description": "changes phone number for the specified contact, requires 'name', 'old phone number' and 'new phone number'",
    },
    "change-birthday": {
        "handler": contact_handlers.change_birthday,
        "description": "changes birthday date for the specified contact, requires 'name' and 'birthday date'",
    },
    "change-email": {
        "handler": contact_handlers.change_email,
        "description": "changes email for the specified contact, requires 'name' and 'email'",
    },
    "change-address": {
        "handler": contact_handlers.change_address,
        "description": "changes address info for the specified contact, requires 'name' and 'address'",
    },
    "delete-contact": {
        "handler": contact_handlers.delete_contact,
        "description": "deletes contact, requires 'name'",
    },
    "delete-phone": {
        #can't delete if one phone record remains
        "handler": contact_handlers.delete_phone,
        "description": "deletes phone number of the specified contact, requires 'name' and 'phone number'",
    },
    "show-all-contacts": {
        #add optional search by name
        "handler": contact_handlers.show_all,
        "description": "shows all contacts info in the address book",
    },
    "search-contacts-by-phone": {
        "handler": contact_handlers.search_by_phone,
        "description": "shows all contacts info in the address book",
    },
    "search-contacts-by-email": {
        "handler": contact_handlers.search_by_email,
        "description": "shows all contacts info in the address book",
    },
    "show-phone": {
        "handler": contact_handlers.show_phone,
        "description": "shows all phone numbers for the specified contact, requires 'name'",
    },
    "show-birthday": {
        "handler": contact_handlers.show_birthday,
        "description": "shows birthday info for the specified contact, requires 'name'",
    },
    "upcoming-birthdays": {
        "handler": contact_handlers.birthdays,
        "description": "shows upcoming birthdays in the next week or 'number of days' specified by the user",
    },
}
