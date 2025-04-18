import random

types = ("rock", "paper", "scissors")
# rules = {
#     "rock": "scissors",
#     "paper": "rock",
#     "scissors": "paper",
# }
rules = {types[i]: types[i-1] for i in range(len(types))}


def game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == 'q':
            break
        elif user_input not in types:
            print("Please type any of [Rock, Paper, Scissors, Q].")
            continue

        computer_input = types[random.randrange(3)]
        print("Computer choose: {}".format(computer_input))
        
        if rules[user_input] == computer_input:
            user_wins += 1
            print("User won.")
        elif rules[computer_input] == user_input:
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

game()