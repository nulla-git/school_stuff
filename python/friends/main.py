friends = ["goff", "maddix", "dylan", "annabelle", "ramon"]
me = "blake"

print(friends)
print("")
for x in friends:
   if x == "dylan":
#continue here will restart the loop instead of continuing it.
#i almost wonder if the person who made this language made it so
#other hackers could atone for their sins, like refusing to write the
#simplest of documentation.
       continue
   print(x)

for x in me:
    print(x)
