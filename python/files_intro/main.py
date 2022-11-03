#blake reneau 2/11/2
#file printing example
import random

foo = open("drinks.txt", "r")
bar = open("poisons.txt", "r")
yum = []
yuck = []
yum = foo.read().splitlines()
yuck = bar.read().splitlines()
yum_rand = random.choices(yum)
yuck_rand = random.choices(yuck)
print("random item from yum: " + str(yum_rand))
print("random item from yuck: " + str(yuck_rand))


"""
print("here's some drinks that i like: ")
print(foo.read()) 
print("and here's just some comestibles in general that i don't like: ")
print(bar.read())
"""

"""
" proof of concept teacher made me do
"
"i = 0
"while i < 11:
"    print(foo.readline())
"    i += 1
"""
