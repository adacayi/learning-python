# If we change this file name to numbers then we can not debug and have an error. There might be a conflict
x = 423425364564562345234534545647456474567
y = 3.0
z = 2 + 1j

print("type(x) =", type(x))
print("type(y) =", type(y))
print("type(z) =", type(z))

i = 1
print("bit_length() of 1 =", i.bit_length())
i = 2
print("bit_length() of 2 =", i.bit_length())
i = 3
print("bit_length() of 3 =", i.bit_length())

print("bit_length() of", x, "=", x.bit_length())

print()
print(x)
print(z * z)

y = 23e-12
print("value = ", y, " type =", type(y))
