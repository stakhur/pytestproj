import random

def new_game():
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please type the number greater than 0 next time.")
            return
    else:
        print("Please type a number next time.")
        return
    number = random.randrange(top_of_range+1)

    tries = 0
    min_num = 0
    max_num = top_of_range
    while True:
        player_guess = input("Input next try [{} - {}]: ".format(min_num, max_num))
        if not player_guess.isdigit():
            print("Please type a number")
            continue

        player_guess = int(player_guess)
        tries += 1
        if player_guess < number:
            if (player_guess >= min_num):
                min_num = player_guess + 1
            print("Nope. The number is greater than {}.".format(player_guess))
        elif player_guess > number:
            if player_guess <= max_num:
                max_num = player_guess - 1
            print("Nope. The number is lower than {}.".format(player_guess))
        else:
            print("Yeah! You are won. The number was {}. You have {} tries.".format(number, tries))
            break

new_game()
