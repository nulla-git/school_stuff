#blake reneau 2/11/22
#file printing example

foo = open("drinks.txt", "r")
#print(foo.read()) 


i = 0
while i < 11:
    print(foo.readline())
    i += 1

