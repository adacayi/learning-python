from datetime import datetime


class Person:
    person_country = "UK"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def print_age(birth_year):
        print("Age for the year %s" % birth_year, datetime.now().year - birth_year)


p1 = Person("Ahmet")
p1.person_country = "France"
p1.print_age(1981)
Person.print_age(1981)
