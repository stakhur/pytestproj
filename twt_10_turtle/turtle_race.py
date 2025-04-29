import random
import time
import turtle

from typing import List


WIDTH, HEIGHT = 1500, 1500
START_Y = -HEIGHT / 2 + 100
FINISH_Y = HEIGHT / 2 - 50
COLORS = ["red", "green", "blue", "brown", "yellow", "pink", "aqua", "orange", "purple", "black"]
MAX_TURTLES = len(COLORS)


def get_number_of_racers(max_racers = MAX_TURTLES) -> int:
    racers = -1
    while not isinstance(racers, int) or racers < 2 or racers > max_racers:
        racers = input(f"How many racers would you like to race (2-{max_racers})?: ")
        if racers.isdigit():
            racers = int(racers)

    return racers


def init_turtle():
    screen = turtle.Screen()
    screen.title("Turtle Racing")
    screen.setup(WIDTH, HEIGHT)


def get_new_racer(color, pos) -> turtle.Turtle:
    racer = turtle.Turtle("turtle")
    racer.color(color)
    racer.width(3)
    racer.left(90)
    racer.penup()
    racer.goto(pos)
    racer.pendown()
    
    return racer


def prepare_racers(num_of_racers) -> List[turtle.Turtle]:
    racers = []
    random.shuffle(COLORS)
    colors = COLORS[:num_of_racers]
    step = WIDTH / (num_of_racers + 1)
    for racer_id in range(num_of_racers):
        pos_x = -WIDTH / 2 + (step + racer_id * step)
        racer = get_new_racer(colors[racer_id], (pos_x, START_Y))
        racers.append(racer)
    
    return racers


def race(racers: List[turtle.Turtle]) -> turtle.Turtle:
    winner = None
    while winner is None:
        for racer in racers:
            distance = random.randint(10, 30)
            racer.forward(distance)
            if racer.pos()[1] >= FINISH_Y:
                winner = racer
                break

    return winner


def winner_dance(racer: turtle.Turtle):
    print(f"{racer.color()[0].capitalize()} turtle won the race!")
    racer.penup()
    racer.left(90)
    racer.forward(50)
    racer.right(180)
    racer.forward(100)
    racer.left(180)
    racer.forward(50)
    racer.right(90)


def game():
    print("Welcome to turtle racing! Please enter the following information.")
    num_of_racers = get_number_of_racers()
    init_turtle()
    racers = prepare_racers(num_of_racers)
    winner = race(racers)
    winner_dance(winner)


if __name__ == "__main__":
    game()
    time.sleep(1)
