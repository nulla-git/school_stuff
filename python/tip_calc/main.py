#Blake Reneau 09/01/2022
#a simple tip calculator

gross = input("price of meal? ")
gross = int(gross)
tip = gross / 5
print("\n")

print("tip at 20%: $", tip)
print("total price: $", tip + gross)
