#Blake Reneau 9/8/22
#a simple program to automatically grade a score.

score = int(input("what's the score? "))

if 40 > score:
    print("Grade is U.")
if 40 <= score >= 59:
    print("Grade is C.")
if 69 <= score >=79:
    print("Grade is B.")
if 80 <= score:
    print("Grade is A.")

#notice that else here has a colon immediately in front of it,
#unlike if where the colon is at the end of the statement.

if score < 40:
    print("Retake Required")
else: print("Pass")
