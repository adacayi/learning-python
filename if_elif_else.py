values = {1: 2, 5: 4, 3: 3}
for a, b in values.items():
    if a > b:
        print(a, ">", b)
    elif b > a:
        print(a, "<", b)
    else:
        print(a, "=", b)

a = 2
b = 3
if a < b: print(a, "<", b)  # Shorthand for one line if statement
# print(a, ">=", b) if a >= b else print(a, "<", b)  # Does not work for Python 2
# Shorthand for one line if else statement with multiple else
# print(a, ">", b) if a > b else print(a, "<", b) if (a < b) else print(a, "=", b) # Does not work for Python 2

if a < b or a == b:
    print(a, "<=", b)

if a <= b and a != b:
    print(a, "<", b)
