car = {
        "brand": "Ford",
        "model": "Mustand",
        "year": 1964
}

print(car)

print(car.get("brand"))
print(car["year"])
car["year"] = 2020
print(car)
print(car["year"])
car["color"] = "red"
car.pop("model")
print(car)
car.clear()
print(car)
