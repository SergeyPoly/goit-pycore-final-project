import pickle
from pathlib import Path
from src.classes import AddressBook

base_path = Path(__file__).parent

def save_data(book, filename="data"):
    file_path = Path(f"{base_path}/data/{filename}.pkl")
    file_path.parent.mkdir(exist_ok=True, parents=True)

    with open(file_path, "wb") as file:
        pickle.dump(book, file)


def load_data(filename="data"):
    file_path = Path(f"{base_path}/data/{filename}.pkl")
    
    if file_path.exists():
        with open(file_path, "rb") as file:
            return pickle.load(file)
        
    return AddressBook()