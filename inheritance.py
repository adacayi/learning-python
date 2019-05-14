class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print_info(self):
        print self.name, self.last_name


adam = Person("Adam", "Smith")
adam.print_info()


class Student(Person):
    pass


jane = Student("Jane", "Walker")
jane.print_info()


class Student(Person):
    def __init__(self, name, last_name, lessons):
        Person.__init__(self, name, last_name)
        self.lessons = lessons

    def print_info(self):
        lesson_string = ""

        i = 0

        for lesson in self.lessons:
            i += 1
            lesson_string += lesson + ", "

        if i > 0:
            lesson_string = lesson_string[0:len(lesson_string) - 2] + "."

        print self.name, self.last_name, "with lessons", lesson_string


sarah = Student("Sarah", "Williams", ["Math", "English"])
sarah.print_info()
