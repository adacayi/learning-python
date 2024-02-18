print("Enter your name")
name = input()
print("Enter your age")
age = int(input())
print("Hello", name, "at age", age)
print("Hello {} at age {}".format(name, age))
print("Hello %s at age %d" % (name, age))

x = "this is a string"
y = 'this is another string with single quotes'

print(x, "\n" + y, "\n")
print(x[0], x[1] + "\n")
print(x[0:3] + "\n")

x = "      String with whitespaces.    "
print(x.strip(), "Strip removes whitespaces on both ends")
print(x)  # Remember that string is immutable
print(x.lstrip(), "Removes only the whitespaces at the beginning of the string")
print(x.rstrip(), "Removes only the whitespaces at the end of the string")

print()
x = "Adam"
print(len(x), "is the length of the string", x)
print(x.lower())
print(x.upper())
print(x.replace("Ad", "Mad"))  # Replace is case sensitive while finding the content to replace

x = "Adam,John,Sarah"
x = x.split(",")
print(x[0], x[2])
