import pickle
from pathlib import Path
from src.classes import AddressBook, NoteBook

file_path = Path(__file__).parent / "cache.pkl"


def save_data(*args):
    with open(file_path, "wb") as file:
        pickle.dump(args, file)


def load_data() -> tuple[AddressBook, NoteBook]:
    if file_path.exists():
        with open(file_path, "rb") as file:
            return tuple(pickle.load(file))

    return (AddressBook(), NoteBook())
