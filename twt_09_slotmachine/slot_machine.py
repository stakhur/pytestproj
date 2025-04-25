import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

win_multiplier = {
    1: 10,
    2: 100,
    3: 1000
}

def get_slot_machine_spin(rows, cols, symbols):
    lines = [['' for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):

        available_symbols = []
        for symb, count in symbols.items():
            available_symbols += [symb] * count

        for c in range(cols):
            symb = random.choice(available_symbols)
            available_symbols.remove(symb)
            lines[r][c] = symb

    return lines

def show_slot_machine_spin(lines):
    for line in lines:
        print(' | ', end="")
        for item in line:
            print(item, end=' | ')
        print()

def get_win_lines(lines):
    win_lines = 0
    for line in lines:
        if len(set(line)) == 1:
            win_lines += 1

    return win_lines


def deposit():
    amount = -1
    while not isinstance(amount, int) or amount <= 0:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)

    return amount


def get_number_of_lines(last_choose = -1):
    last_choose_msg = ""
    if last_choose != -1:
        last_choose_msg = f". Or press Enter to use previous choose: {last_choose} line(s)"

    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}){last_choose_msg}: ")
        if lines == "" and last_choose != -1:
            lines = last_choose
            break

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter a number.")

    return lines


def get_bet(last_choose = -1):
    last_choose_msg = ""
    if last_choose != -1:
        last_choose_msg = f" Press Enter to use previous bet: ${last_choose}:"

    while True:
        bet = input(f"What would you like to bet on each line?{last_choose_msg} $")
        if bet == "" and last_choose != -1:
            bet = last_choose
            break

        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number.")

    return bet


def main():
    balance = deposit()
    lines = -1
    bet = -1
    
    while balance > 0:
        answ = input(f"Your balance is ${balance}. Do you want to play (Y/n)? ").lower()
        if answ not in ["n", "", "y"]:
            continue
        elif answ == "n":
            break

        while True:
            lines = get_number_of_lines(lines)
            bet = get_bet(bet)
            total_bet = bet * lines
            if total_bet <= balance:
                break
            else:
                print(f"You do not have enouth money on your balance. Bet: ${total_bet}, balance: ${balance}!")

        balance -= total_bet
        print(f"You bet ${bet} on {lines} line(s). Total bet is ${total_bet}")

        spin = get_slot_machine_spin(ROWS, COLS, symbol_count)
        show_slot_machine_spin(spin)
        win_lines = get_win_lines(spin)

        if win_lines:
            my_lines_win = win_lines if (lines > win_lines) else (win_lines - (win_lines - lines))

            win_money = win_multiplier[my_lines_win] * bet
            balance += win_money
            print(f"Congratulation! {win_lines} line(s) won! You bet on {lines} line(s). You win ${win_money}")
        else:
            print(f"0 lines won. You loose ${total_bet}")

    print(f"Thank you for playing! Your balance is ${balance}. Bye.")


if __name__ == "__main__":
    main()