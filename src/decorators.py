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
            if func.__name__ == "add_contact" or func.__name__ == "add_phone" or func.__name__ == "delete_phone":
                return "Enter name and phone please."
            
            if func.__name__ == "add_birthday":
                return "Enter name and birthday date."
            
            if func.__name__ == "add_email":
                return "Enter name and email."
            
            if func.__name__ == "add_address":
                return "Enter name and address."
            
            if func.__name__ == "change_phone":
                return "Enter name, old phone and new phone please."
            
        except IndexError:
            return "Enter name please."
        except KeyError as e:
            return f"No such name: {e} in contacts"
        except (ValidationError, NotFoundError) as e:
            return e

    return inner


def show_all_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError:
            return "No contacts available."
        except ValueError:
            return "Enter a positive integer please, min value 1."
        except IndexError:
            return "Enter search condition please."

    return inner