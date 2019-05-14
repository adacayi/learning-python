"""
This is a multiline documentation
This is the first code for Python
"""
x = 3
y = x - 2

if x != y:
    print(x, "does not equal", y, "\n\n")  # One line comment. Print puts a space in the output between its parameters

name = "Adam"
surname = "Smith"
fullName = name + " " + surname

print("Hi", name, surname)  # Be aware of the spaces added between the parameters
print("Hi " + fullName)
