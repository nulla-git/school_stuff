#Blake Reneau 10/5/2022
#total price calculator for a fake water park.
print("Entrance Ticket Price Chart:")
print("Adult: $15")
print("Child: $10 (Younger than 18)")
print("If your entry tickets are higher than or equal to 50,\nthen you are automatically granted a 5% discout.")

adults = int(input("how many adults? "))
children = int(input("how many children? "))

adults *= 15
children *= 11
total = (adults + children)

if total > 50:
    total = total * .95
    round(total, 2)
#keep this in mind, it might be useful months, weeks, years, days, idk, but remember it. 
    print("your total with a discout is $" + str(total))
elif total <= 50:
    print("your total is $" + str(total))

print("have a great day!")
