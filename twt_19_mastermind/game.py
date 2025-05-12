# Input initial positions from user2
# Print "Welcome to Mastermind. Attempt to guess the 4 digit code... You have 10 tries"
# Print "The colors that could make up the code are: R G B Y W O"
# Print "Guess (space separated): "
# Print "Correct position: A | Incorrect position: B"
# ...
# Print "You guessed the code in T tries"

# get initial positions to guess
AVAILABLE_COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGHT = 4

def get_code(message):
    code = None
    while True:
        code = input(message).split()
        if len(code) != CODE_LENGHT:
            print(f"Code must be {CODE_LENGHT}-length symbols, separated by space!")
            continue
        
        for c in code:
            if c not in AVAILABLE_COLORS:
                print(f"Code must be consist only from the following symbols: {AVAILABLE_COLORS}!")
                break
        else:
            break

    return code


def check_guess(code, guess):
    buf = code[:]
    correct, incorrect = 0, 0

    for ig, g in enumerate(guess):   # G U E S S   R R O B
        for ic, c in enumerate(buf): # C O D E E   B B Y Y
            if guess[ig] == buf[ig]:
                buf[ig] = '-'
                correct += 1
                break
            elif g == c:
                if guess[ic] == buf[ic]:
                    continue
                else:
                    buf[ic] = '-'
                    incorrect += 1
                    break

    return correct, incorrect
            


def game():
    code = get_code(f"Enter initial {CODE_LENGHT}-length code (space separated) using {AVAILABLE_COLORS} symbols: ")
    print(f"Welcome to Mastermind. Attempt to guess the {CODE_LENGHT} digit code... You have {TRIES} tries")
    print(f"The colors that could make up the code are: {" ".join(AVAILABLE_COLORS)}")
    tries = 1
    
    while tries <= TRIES:
        guess = get_code("Guess (space separated): ")
        correct, incorrect = check_guess(code, guess)
        if correct == CODE_LENGHT:
            break
        
        print(f"Correct position: {correct} | Incorrect position: {incorrect}")
        tries += 1

    if tries <= TRIES:
        print(f"You guessed the code in {tries} tries!")
    else:
        print(f"Sorry. The right code was {" ".join(code)}")

if __name__ == "__main__":
    game()