x = int(2.8)
print(x, " ", type(x), "\n")

x = int("345345")  # If the string in the int constructor is a float, it gives runtime error
print(x, " ", type(x), "\n")

x = float("345345.234")
print(x, " ", type(x), "\n")

x = str(x)

print(x + " is now a ", type(x), "\n")
