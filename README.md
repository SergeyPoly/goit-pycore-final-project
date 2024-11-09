# Personal Assistant Bot (DEMO)

## Description

A DEMO version of Personal Assistant Bot - command-line tool designed to assist you in organizing your contacts and notes efficiently. It allows you to easily manage and access contacts information (name, phone numbers, birthday, email address, and physical address) and additionally, to manage your personal notes as well as categorize them by titles or tags for better organization. Application works offline and doesn't require stable internet connection. All data is stored locally on your PC thus information remains secure and accessible whenever you need it.

## Installation

1. git clone https://github.com/SergeyPoly/goit-pycore-final-project.git

2. pip install .

3. enter command `run_demo`. 


### Common Commands
| Command | Description            | 
| --------| ---------------------- |
| `help`  | shows all menu options |  
| `exit`  | exit the application   |    
                   

### Contacts Commands
| Command                    | Description        | Parameters                       |
| -------------------------- | ------------------ | -------------------------------- |
| `add-contact`              | adds a new contact | `name` `phone number` (required) |
| `add-phone`                | adds additional phone number to the specified contact | `name` `phone number` (required) |
| `add-birthday`             | adds/changes birthday date to the specified contact | `name` `birthday date` (required) |
| `add-email`                | adds/changes email to the specified contact | `name` `email` (required) |
| `add-address`              | adds/changes address info to the specified contact | `name` `address` (required) |
| `change-phone`             | changes phone number for the specified contact | `name` `old phone number` `new phone number` (required) |
| `delete-contact`           | deletes contact | `name` (required) |
| `delete-phone`             | deletes phone number of the specified contact | `name` `phone number` (required) |
| `show-all-contacts`        | shows all contacts info, filters by 'name' if search option specified by the user | `name` (optional) |
| `show-contact`             | shows contact searched by the name | `name` (required) |
| `search-contacts-by-phone` | shows contacts info, filtered by the phone number | `phone number` (required) |
| `search-contacts-by-email` | shows contacts info, filtered by the email | `email` (required) |
| `show-phone`               | shows all phone numbers for the specified contact | `name` (required) |
| `show-birthday`            | shows birthday info for the specified contact | `name` (required) |
| `upcoming-birthdays`       | shows upcoming birthdays in the next week or 'number of days' specified by the user | `number of days` (optional) |


### Notebook Commands
| Command                    | Description     | Parameters                      |
| -------------------------- | --------------- | ------------------------------- |
| `add-note`                 | adds a new note | `name` `description` (required) |
| `edit-note`                | edits note's description | `description` (required) |
| `find-note`                | shows specific note | `name` (required) |
| `delete-note`              | deletes note | `name` (required) |
| `add-note-tag`             | adds a tag to a note | `name` `tag` (required) |
| `remove-note-tag`          | removes a tag from a note | `name` `tag` (required) |
| `show-all-notes`           | shows all notes | |
| `show-notes-by-tag`        | shows all notes that have cpecified tag | `tag` (required) |


## Technologies Used
- [Python](https://www.python.org/): an interpreted, object-oriented, high-level programming language with dynamic semantics.
- [Python Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io): a library for building powerful interactive command line and terminal applications in Python.
- [PrettyTable](https://pypi.org/project/prettytable/): a simple Python library for easily displaying tabular data in a visually appealing ASCII table format.
- [Colorama](https://pypi.org/project/colorama/): cross-platform colored terminal text.
- [Wcwidth](https://pypi.org/project/wcwidth/): measures the displayed width of unicode strings in a terminal.


### Корисні скрипти:
- `bash scripts/init_venv.sh` - ініціалізує .venv середовище (вмикає venv)
- `bash scripts/save_requirements.sh` - зберігає поточний стан пакетів pip
- `bash scripts/install_requirements.sh` - встановлює необхідні пакети pip (вмикає venv)
- `deactivate` - вимикає venv
