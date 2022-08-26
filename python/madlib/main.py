#Blake Reneau 8/26/2022
#program to generate a finished mad lib

story = "Dear Santa, I have been a very {} {} this year. I have helped my {} and {} with chores around the {}. I {} the {} and clean the {} every day. I would really like to be on the {} list this year! I would love a {} new {} for Christmas. If you could put a {} inside of my stocking that is hanging on the {}, that would be {}! I am very {} for your visit and will leave out {} and {} for you and some {} for your reindeer. Merry {}! From {}."

name = input("what's your name?: ")
print("")
noun1 = input("need a noun: ")
noun2 = input("I need another: ")
noun3 = input("and another noun... ")
noun4 = input("and another noun... ")
noun5 = input("and another noun... ")
noun6 = input("and another noun... ")
noun7 = input("and another noun... ")
print("")
verb = input("Now I need a verb: ")
print("")
emotion = input("now I need an emotion: ")
print("")
adj1 = input("Now I need an adjective: ")
adj2 = input("and another: ")
adj3 = input("and another: ")
adj4 = input("and another: ")
print("")
reltv1 = input("Now a name of a relative: ")
reltv2 = input("and another: ")
print("")
food1 = input("Now I need a food: ")
food2 = input("and another: ")
print("")
holiday = input("I need a holiday: ")
print("")
drink = input("Finally, I need a drink: ")
print("")
print("--------------------")
print("")
test = "test"


print(story.format(adj1, noun1, reltv1, reltv2, noun2, verb, noun3, noun4, adj2, adj3, noun4, noun5, noun6, adj4, emotion, food1, drink, food2, holiday, name)) 