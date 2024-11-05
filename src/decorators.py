from functools import wraps
from src.classes import ValidationError, NotFoundError

def parse_command_error(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return ['error']

    return inner


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Enter name and phone please."
            
            if func.__name__ == "change_contact":
                return "Enter name, old phone and new phone please."
            
            if func.__name__ == "add_birthday":
                return "Enter name and birthday date."
            
        except IndexError:
            return "Enter name please."
        except KeyError as e:
            return f"No such name: {e} in contacts"
        except (ValidationError, NotFoundError) as e:
            return e

    return inner


def show_all_error(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return "No contacts available."

    return inner