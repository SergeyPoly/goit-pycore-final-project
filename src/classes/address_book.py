from collections import UserDict
from datetime import datetime, timedelta
from .record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if self.find(name):
            del self.data[name]

    def get_upcoming_birthdays (self) -> list[dict]:
        upcoming_birthdays = []
        current_date = datetime.today().date()
        current_year = datetime.now().year
        target_date = current_date + timedelta(days=7)

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
