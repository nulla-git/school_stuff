#Blake Reneau 9/14/2022
#a simple store simulation

A = 1.50
B = 2.50
C = 2.00
D = 9.50
E = 2000000.00

print("Price list")
print("A. dog food - $1.50")
print("B. cat food - $2.50")
print("C. hamster food - $2.00")
print("D. horse food - $9.50")
print("E. Thermonuclear Reactor - $2,000,000")
print("input X to exit(or crash the program")
print("")
money = float(input("how much do you have to spend? "))

while money > 0:
    item = input("wha'd'ya want? (input the letter) ")
    if item == "X":
        print("hah, broke")
        break
    else:
        quantity = int(input("how many? "))
        cost = 0
        if item == "A":
            cost = A * quantity
        elif item == "B":
            cost = B * quantity
        elif item == "C":
            cost = C * quantity
        elif item == "D":
            cost = D * quantity
        elif item == "E":
            cost = E * quantity
        
        if money >= cost:
            money = money - cost
            break
        else:
            print("ha, broke")

print("money left:" + str(money))
print("bye")
