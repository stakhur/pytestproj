import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def get_players():
    max_players = 5
    num_of_players = ""

    while not isinstance(num_of_players, int) or (num_of_players < 2 or num_of_players > max_players):
        num_of_players = input(f"Type number of players (2 - {max_players}): ")
        if num_of_players.isdigit():
            num_of_players = int(num_of_players)
    
    return num_of_players

def game():
    POINTS_TO_WIN = 50
    players = get_players()
    players_scores = [0 for i in range(players)]

    current_player_id = 0
    while all(x < POINTS_TO_WIN for x in players_scores):
        current_player_scores = 0
        while True:
            choose = input(f"Player {current_player_id + 1} turn.\n"
                           f"You have {players_scores[current_player_id]} points total. "
                           f"You can save {current_player_scores} points from this round.\n"
                           "Do you want to roll (Y/n)? ").lower()
            if choose not in ("n", "y"):
                continue

            if choose == "n":
                players_scores[current_player_id] += current_player_scores
                print(f"You saved {current_player_scores} points. "
                      f"You have {players_scores[current_player_id]} points total.")
                if players_scores[current_player_id] >= POINTS_TO_WIN:
                    print(f"Player {current_player_id + 1} win!")
                break
            else:
                points = roll()
                if points != 1:
                    current_player_scores += points
                    print(f"You earn {points} points!")
                else:
                    current_player_scores = 0
                    print("It is 1. You loose your points :(")
                    break
        
        current_player_id += 1
        if current_player_id >= players:
            current_player_id = 0
    
    print(players_scores)

game()