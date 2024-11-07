from collections import UserDict
from datetime import datetime, timedelta
from .record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find(self, name: str, rise_error: bool = False) -> Record:
        record = self.data.get(name)

        if record is None and rise_error:
            raise KeyError(name)
        
        return record
    
    def delete(self, name: str) -> None:
        self.find(name, True)
        del self.data[name]

    def search_by_phone(self, search_fragment: str) -> list[dict]:
        found_records = []

        for record in self.data.values():
            if search_fragment in map(lambda phone: phone.value, record.phones):
                found_records.append(record)
   
        return found_records
    
    def search_by_email(self, search_fragment: str) -> list[dict]:
        found_records = []

        for record in self.data.values():
            if record.email and search_fragment == record.email.value:
                found_records.append(record)
   
        return found_records

    def get_upcoming_birthdays (self, days: int) -> list[dict]:
        upcoming_birthdays = []
        current_date = datetime.today().date()
        current_year = datetime.now().year
        target_date = current_date + timedelta(days)

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=current_year)

                if current_date <= birthday_this_year <= target_date:
                    congratulation_info = {
                        "name": record.name.value,
                        "birthday": record.birthday.value.strftime("%d.%m.%Y")
                    }
                    weekday = birthday_this_year.weekday()

                    if weekday < 5:
                        congratulation_info["congratulation_date"] = birthday_this_year.strftime("%d.%m.%Y")
                    else:
                        congratulation_info["congratulation_date"] = (birthday_this_year + timedelta(days=(7-weekday))).strftime("%d.%m.%Y")

                    upcoming_birthdays.append(congratulation_info)
   
        return upcoming_birthdays
