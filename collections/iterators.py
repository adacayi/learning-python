fruits = ["apple", "banana", "orange"]
iterator = iter(fruits)
print next(iterator)
print next(iterator)
print next(iterator)


# next(iterator) # This line would give an error since all the values are iterated and StopIteration is returned


class Fruits:
    fruits = ["apple", "banana", "orange"]

    def __iter__(self):
        self.i = 0
        return self

    def next(self):
        if self.i >= len(self.fruits):
            raise StopIteration

        current = self.fruits[self.i]
        self.i += 1
        return current


fruits = Fruits()
iterator = iter(fruits)

print next(iterator)
print next(iterator)
print next(iterator)

print

for fruit in fruits:
    print(fruit)
