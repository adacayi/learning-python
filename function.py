def greeting():
    print("Hello")


greeting()


def factorial(a):
    result = 1
    for x in range(1, a + 1):
        result *= x
    return result


print(factorial(3))


def greeting(name, country="UK"):
    print "Hello", name, "from", country


greeting("Peter")
greeting("Adam", 3.234)


def factorial(a):
    if a <= 1:
        return 1

    print("recursive")

    return a * factorial(a - 1)


print(factorial(2))

# del factorial

# print(factorial(3))# This will give a not defined error
