from src.handlers import contact_handlers

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
        "description": "adds/changes birthday date to the specified contact, requires 'name' and 'birthday date'",
    },
    "add-email": {
        "handler": contact_handlers.add_email,
        "description": "adds/changes email to the specified contact, requires 'name' and 'email'",
    },
    "add-address": {
        "handler": contact_handlers.add_address,
        "description": "adds/changes address info to the specified contact, requires 'name' and 'address'",
    },
    "change-phone": {
        "handler": contact_handlers.change_phone,
        "description": "changes phone number for the specified contact, requires 'name', 'old phone number' and 'new phone number'",
    },
    "delete-contact": {
        "handler": contact_handlers.delete_contact,
        "description": "deletes contact, requires 'name'",
    },
    "delete-phone": {
        "handler": contact_handlers.delete_phone,
        "description": "deletes phone number of the specified contact, requires 'name' and 'phone number'",
    },
    "show-all-contacts": {
        "handler": contact_handlers.show_all,
        "description": "shows all contacts info in the address book, filters by 'name' if search option specified by the user",
    },
    "show-contact": {
        "handler": contact_handlers.show_contact,
        "description": "shows contact by the name",
    },
    "search-contacts-by-phone": {
        "handler": contact_handlers.search_by_phone,
        "description": "shows all contacts info in the address book, filtered by phone number",
    },
    "search-contacts-by-email": {
        "handler": contact_handlers.search_by_email,
        "description": "shows all contacts info in the address book, filtered by email",
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
