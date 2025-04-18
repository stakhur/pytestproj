import random

goptions = ("rock", "paper", "scissors")
# rules = {
#     "rock": "scissors",
#     "paper": "rock",
#     "scissors": "paper",
# }
grules = {goptions[i]: goptions[i-1] for i in range(len(goptions))}


def game(options, rules):
    user_wins = 0
    computer_wins = 0

    while True:
        user_input = input("Type {} or Q to quit: ".format("/".join(options))).lower()
        if user_input == 'q':
            break
        elif user_input not in options:
            print("Please type any of [{}, Q].".format(", ".join(options)))
            continue

        computer_pick = options[random.randrange(3)]
        print("Computer picked:", computer_pick + ".")
        
        if rules[user_input] == computer_pick:
            user_wins += 1
            print("User won.")
        elif rules[computer_pick] == user_input:
            computer_wins += 1
            print("Computer won.")
        else:
            print("Draw.")
        print()

    # Show game results    
    print("User score: {}. Computer score: {}".format(user_wins, computer_wins))
    result = ""
    if user_wins > computer_wins:
        result = "User won!"
    elif user_wins < computer_wins:
        result = "Computer won!"
    else:
        result = "Draw."
    print("Game results: {}".format(result))

game(goptions, grules)