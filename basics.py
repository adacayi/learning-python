"""
This is a multiline documentation
This is the first code for Python
"""
x = 3
y = x - 2

if x != y:
    print(x, "does not equal to", y)  # One line comment. Print puts a space in the output between its parameters and puts a newline at the end. You can override this behavior by setting sep = "some separator", which can also be set to empty string and you can set end = ""
    print(x, "does not equal to", y, sep = "-", end = "+++")
    print(x, "does not equal to", y, sep = "")

name = "Adam"
surname = "Smith"
fullName = name + " " + surname

print("Hi", name, surname)
print("Hi " + fullName)
