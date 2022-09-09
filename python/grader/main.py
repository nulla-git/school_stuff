#Blake Reneau 9/8/22
#a simple program to automatically grade a score.
import sys

score = int(input("what's the score? "))

#this logic should work but it doesn't.
#it's commented out for now, may look at it later. 

# if score > 100 or < 0:
#    print("invalid!")
#    sys.exit()

#elif simply means else if a condition is met.

if score < 40:
    print("Grade is U.")
elif 40 <= score <= 59:
    print("Grade is C.")
elif 60 <= score <= 79:
    print("Grade is B.")
elif 80 <= score:
    print("Grade is A.")

#notice that else here has a colon immediately in front of it,
#unlike if where the colon is at the end of the statement.

if score < 40:
    print("Retake Required")
else: print("Pass")
