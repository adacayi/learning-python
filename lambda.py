power = lambda x, y: x ** y
print power(3, 4)


def multiply(times):
    return lambda x: x * times


double = multiply(2)
triple = multiply(3)
print(double(3))
print(triple(5))

