for letter in "banana":
    if letter == "a":
        continue

    print(letter)

    if letter == "n":
        break

print()

for i in range(4):
    print(i)

print()
for i in range(4, 6):
    print(i)

print()

for i in range(1, 11, 2):
    print(i)

adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)
