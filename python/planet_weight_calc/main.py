#Blake Rneeau 9/28/22
#a simple program to calculate someone's weight on another planets

earthKg = float(input("what is your weight? "))
divEarthKg = earthKg / 9.81

#the round function rounds the first number input, and rounds to the decimal place specified.

moon = round((divEarthKg * 1.622), 2)
mercury = round((divEarthKg * 3.7), 2)
venus = round((divEarthKg * 8.87), 2)
mars = round((divEarthKg * 3.711), 2)
jupiter = round((divEarthKg * 24.79), 2)
saturn = round((divEarthKg * 10.44), 2)
uranus = round((divEarthKg * 8.69), 2)
neptune = round((divEarthKg * 11.15), 2)

print("Moon weight:",moon,"kg")
print("Mercury weight:",mercury,"kg")
print("Venus weight:",venus,"kg")
print("Mars weight:",mars,"kg")
print("Jupiter weight:",jupiter,"kg")
print("Saturn weight:",saturn,"kg")
print("Uranus weight:",uranus,"kg")
print("Neptune weight:",neptune,"kg")

