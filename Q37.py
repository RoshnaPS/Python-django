from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def display_details(self):
        age = self.calculate_age()
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.dob}")
        print(f"Age: {age} years")

person1 = Person("Jack", "USA", "2000-11-15")
person1.display_details()
person2 = Person("Bubblu", "Canada", "1999-08-26")
person2.display_details()