from functools import wraps
from src.classes import MenuOutput


def with_empty_args_handler(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return [ MenuOutput.print_error_message("unknown"), []]

    return inner


def with_input_error_handler(value_error_text: str | None = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                return MenuOutput.print_error_message(value_error_text or str(e))
            except Exception as e:
                return MenuOutput.print_error_message(str(e))

        return wrapper

    return decorator


def with_empty_check(book_type: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            book = args[1]
            if not book:
                return MenuOutput.print_error_message(f"No {book_type} available.")

            return func(*args, **kwargs)

        return wrapper

    return decorator
