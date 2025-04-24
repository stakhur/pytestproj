import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem(min_operand = MIN_OPERAND, max_operand = MAX_OPERAND, operators = OPERATORS):
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    
    return expr, answer


def game(total_problems = TOTAL_PROBLEMS):
    input("Press enter to start!")
    print("---------------------")
    start_time = time.time()

    wrong = 0
    for i in range(total_problems):
        expr, answ = generate_problem()
        while True:
            guess = input("problem #" + str(i+1) + ": " + expr + " = ")
            if guess == str(answ):
                break
            wrong += 1

    total_time = round(time.time() - start_time, 2)
    precision = round(100 * total_problems / (wrong + total_problems), 2)
    print("---------------------")
    print(f"Nice work! You finished in {total_time} seconds. You precision is {precision}%")

game()