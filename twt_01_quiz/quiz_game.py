core = [
    # (question, answer, points)
    ("What does CPU mean? ", "central processing unit", 1),
    ("What does GPU mean? ", "graphical processing unit", 1),
    ("What does RAM mean? ", "random access memory", 1),
    ("What does ROM mean? ", "read only memory", 1),
]

def start_quiz_game(model):
    print("Welcome to my computer quiz!")

    # get user input about should we start new game
    answer = input("Do you want to start new game? ")
    if answer.lower() != "yes":
        quit()

    print("Let's play :)")
    score = 0

    for (question, answer, points) in model:
        user_answer = input(question).lower()
        if user_answer == answer:
            print("Correct")
            score += points
        else:
            print("Incorrect")

    print("You got {} question{} correct.".format(score, "" if score == 1 else "s"))
    print("You got {}%.".format((score / len(core)) * 100, "" if score == 1 else "s"))

start_quiz_game(core)