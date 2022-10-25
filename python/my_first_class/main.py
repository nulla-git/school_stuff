#Blake Reneau 10/25/2022
#simple class example

class dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

jacob = dog("jacob", "Corgi", 5, "Black")
molly = dog("molly", "pomeranian", 7, "white")

print(jacob.name + " is a " + jacob.color + ", " + str(jacob.age) + " year old " + jacob.breed)
print(molly.name + " is a " + molly.color + ", " + str(molly.age) + " year old " + molly.breed)


