class Person:
    person_country = "UK"

    def __init__(self, name):
        self.name = name

    @classmethod
    def print_class(cls):
        # print(cls.name) # This would give an error
        print(cls.person_country)


p1 = Person("Ahmet")
p2 = Person("Salih")
p1.person_country = "France"
p2.person_country = "Italy"
p1.print_class()
print("\n")
p2.print_class()

