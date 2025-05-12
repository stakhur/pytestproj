import random

AVAILABLE_COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 2
CODE_LENGHT = 4


def generate_code():
    code = []
    for _ in range(CODE_LENGHT):
        color = random.choice(AVAILABLE_COLORS)
        code.append(color)

    return code


def get_code(message):
    code = None
    while True:
        code = input(message).upper().split()
        if len(code) != CODE_LENGHT:
            print(f"Code must be {CODE_LENGHT}-length colors, separated by space!")
            continue
        
        for color in code:
            if color not in AVAILABLE_COLORS:
                print(f"Code must be consist only from the following colors: {AVAILABLE_COLORS}!")
                break
        else:
            break

    return code


def check_guess(code, guess):
    buf = code[:]
    correct, incorrect = 0, 0

    for guess_id, g in enumerate(guess):   # G U E S S   R R O B
        for code_id, c in enumerate(buf): # C O D E E   B B Y Y
            if guess[guess_id] == buf[guess_id]:
                buf[guess_id] = '-'
                correct += 1
                break
            elif g == c:
                if guess[code_id] == buf[code_id]:
                    continue
                else:
                    buf[code_id] = '-'
                    incorrect += 1
                    break

    return correct, incorrect


def game():
    code = generate_code()
    print(code)
    # code = get_code(f"Enter initial {CODE_LENGHT}-length code (space separated) using {AVAILABLE_COLORS} symbols: ")
    print(f"Welcome to Mastermind. Attempt to guess the {CODE_LENGHT} digit code... You have {TRIES} tries")
    print(f"The colors that could make up the code are: {" ".join(AVAILABLE_COLORS)}")
    
    for tries in range(1, TRIES + 1):
        guess = get_code("Guess (space separated): ")
        correct, incorrect = check_guess(code, guess)
        if correct == CODE_LENGHT:
            print(f"You guessed the code in {tries} tries!")
            break
        
        print(f"Correct position: {correct} | Incorrect position: {incorrect}")
    else:
        print(f"Sorry. The right code was {" ".join(code)}")

if __name__ == "__main__":
    game()