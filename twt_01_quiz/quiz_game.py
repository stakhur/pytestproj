print("Welcome to my computer quiz!")

# get user input about should we start new game
answer = input("Do you want to start new game? ")
if answer.lower() != "yes":
    quit()

print("Let's play :)")
score = 0

answer = input("What does CPU mean? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU mean? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM mean? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM mean? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got {} question{} correct.".format(score, "" if score == 1 else "s"))
print("You got {}%.".format((score / 4) * 100, "" if score == 1 else "s"))