class Student:
    name = ""
    age = 0
    lessons = []

    def print_info(self):
        print(self.name, self.age, self.lessons)


adam = Student()
print("adam =", adam)
print("adam.name =", adam.name)
print("adam.age =", adam.age)
print("adam.lessons =", adam.lessons)
adam.print_info()


class Person:
    def __init__(self, name, age, lessons):
        self.name = name
        self.age = age
        self.lessons = lessons

    def greeting(self):
        print("Greetings to all from", self.name)


adam = Person("Adam", 18, ["English", "Math"])

print("adam =", adam)
print("adam.name =", adam.name)
print("adam.age =", adam.age)
print("adam.lessons =", adam.lessons)
adam.greeting()
adam.age = 20
print("adam.age =", adam.age)
del adam.lessons
# del adam.greeting # methods cannot be deleted
# print(adam.lessons) # This will give a no attribute error
del adam
# print(adam) # This will give a not defined error
