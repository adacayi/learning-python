car = {"brand": "Ford", "model": "Mustang", "year": 2014}
print("car =", car)
print("len(car) =", len(car))
print("car.keys() =", car.keys())
print("car.values() =", car.values())
print("car[\"brand\"] =", car["brand"])
print("car.get(\"brand\") =", car.get("brand"))
car["year"] = 2018
for key in car.keys():
    print(key, "=", car[key])

for key in car:
    print(key, "=", car[key])

for key, value in car.items():
    print(key, "=", value)

if "model" in car:
    print("model key is in car")

car["color"] = "black"
print("car =", car)
print("car.pop(\"color\") =", car.pop("color"))
print("car =", car)
print("car.popItem() =", car.popitem())
print("car =", car)
# del car["brand"] # This cannot be done with Python 2
car.clear()
print("car =", car)
del car
# print("car =",car) # This will give a not defined error

car = {"brand": "Ford", "model": "Mustang", "year": 2014}
newCar = car.copy()
print("newCar is car =", newCar is car)
print("newCar == car", newCar == car)
newCar = dict(car)
print("newCar is car =", newCar is car)
print("newCar == car", newCar == car)
car.update({"color": "red", "volume": 220, "year": 2019})
print("car = ", car)
print("car.setdefault(\"range\", 800) =", car.setdefault("range", 800))
print("car = ", car)
print("car.setdefault(\"color\", \"black\") =", car.setdefault("color", "black"))
print("car = ", car)
