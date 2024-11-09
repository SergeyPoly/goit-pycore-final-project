from functools import wraps
from src.output.pretty_output import print_error_message, print_common_message


def with_empty_args_handler(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return ["unknown", []]

    return inner


def with_input_error_handler(value_error_text: str | None = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print_error_message(value_error_text or str(e))
            except Exception as e:
                print_error_message(str(e))

        return wrapper

    return decorator


def with_empty_check(book_type: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            book = args[1]
            if book:
                return func(*args, **kwargs)

            print_common_message(f"No {book_type} available.")

        return wrapper

    return decorator
