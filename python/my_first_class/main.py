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
mark = dog("mark", "golden retriever", 4, "golden")
bob = dog("bob", "chihuawa", 2, "brown")

print(jacob.name + " is a " + jacob.color + ", " + str(jacob.age) + " year old " + jacob.breed)
print(molly.name + " is a " + molly.color + ", " + str(molly.age) + " year old " + molly.breed)
print(mark.name + " is a " + mark.color + ", " + str(mark.age) + " year old " + mark.breed)
print(bob.name + " is a " + bob.color + ", " + str(bob.age) + " year old " + bob.breed)
