print("5%3 =", 5 % 3)
print("2**4 =", 2 ** 4)
print("9/2 =", 9 / 2)
print("9//2 =", 9 // 2)
x = 3
y = 5
z = 2
print("x < y and z > x =", x < y and z > x)
print("5 < 2 < 3 =", 5 < 2 < 3)  # This is the simplification for 5<2 and 2<3
print("not (y < x) =", not (y < x))
x = ["banana", "apple"]
y = ["banana", "apple"]
print("x is y =", x is y)  # Checks for object equality (if they point the same object)
print("x == y =", x == y)  # Checks for value equality
y = ["banana"]
print("x == y =", x == y)
print("\"apple\" in x = ", "apple" in x)
print("\"banana\" not in y = ", "banana" not in y)
print("10&12 =", 10 & 12)
print("10|12 =", 10 | 12)
x = -2
print("~x =", ~x)
print("5>>1 =", 5 >> 1)
print("4<<3 =", 4 << 3)

"""
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y

=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
//=	x //= 3	x = x // 3
**=	x **= 3	x = x ** 3
&=	x &= 3	x = x & 3
|=	x |= 3	x = x | 3
^=	x ^= 3	x = x ^ 3
>>=	x >>= 3	x = x >> 3
<<=	x <<= 3	x = x << 3

==	Equal	x == y
!=	Not equal	x != y
>	Greater than	x > y
<	Less than	x < y
>=	Greater than or equal to	x >= y
<=	Less than or equal to	x <= y

and 	Returns True if both statements are true	x < 5 and  x < 10
or	Returns True if one of the statements is true	x < 5 or x < 4
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

is 	Returns true if both variables are the same object	x is y
is not	Returns true if both variables are not the same object	x is not y

in 	Returns True if a sequence with the specified value is present in the object	x in y
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""
