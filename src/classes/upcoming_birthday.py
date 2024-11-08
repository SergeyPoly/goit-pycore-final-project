class UpcomingBirthday:
    def __init__(self, name: str, birthday: str, congratulation_date: str):
        self.name = name
        self.birthday = birthday
        self.congratulation_date = congratulation_date

    def __str__(self):
        return f"Contact name: {self.name}, birthday: {self.birthday}, congratulation date: {self.congratulation_date}"
