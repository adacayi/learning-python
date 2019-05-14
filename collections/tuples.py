fruits = ("apple", "orange", "banana")
print("fruits =", fruits)
print("len(fruits) =", len(fruits))
print("fruits[1] =", fruits[1])
# fruits[1]="strawberry" This will give an error since tuples are unchangeable after being generated
newFruits = tuple(fruits)
print("newFruits is fruits =", newFruits is fruits)  # This is not a copy of the fruits, it is the same tuple
print("newFruits == fruits =", newFruits == fruits)
del fruits
# print(fruits) This code would give not defined error
print("newFruits =", newFruits)  # This will work
print("newFruits.count(\"orange\") =", newFruits.count("orange"))
print("newFruits.index(\"banana\") =", newFruits.index("banana"))
