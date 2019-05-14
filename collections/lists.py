fruits = ["apple", "orange", "strawberry"]
print "fruits =", fruits
print"len(fruits)= ", len(fruits)
fruits.append("banana")
fruits.insert(2, "coconut")
fruits.append(2 + 4j)
fruits.remove("orange")

for fruit in fruits:
    print(fruit)

print('"apple" in fruits', "apple" in fruits)
print("2+4j in fruits", 2 + 4j in fruits)
print()
print("fruits =", fruits)
x = fruits.pop()
print("fruits.pop() =", x)
print("fruits.pop(0) =", fruits.pop(0))
print("fruits =", fruits)
del fruits[1]
print("fruits =", fruits)
# fruits.clear() # Clear method does not exist for Python 2
print("fruits =", fruits)
del fruits
# print(fruits) this line will give not defined runtime error

fruits = ["apple", "orange", "strawberry", "apple"]
# newFruits = fruits.copy() # Copy method does not exist for list in Python 2
newFruits = list(fruits)
print("fruits is list(fruits) =", fruits is newFruits)
print("fruits == list(fruits) =", fruits == newFruits)

print('fruits.count("apple") =', fruits.count("apple"))
cars = ["Volvo", "Audi", "McLauren"]
fruits.extend(cars)
print(fruits)
print("fruits.index(\"apple\") =", fruits.index("apple"))
print("fruits.index(\"apple\") =", fruits.index("apple", 1))
fruits.sort()
print("fruits =", fruits)
fruits.reverse()
print("fruits =", fruits)
