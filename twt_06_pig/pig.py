import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def get_players(max_players=5):
    num_of_players = ""

    while not isinstance(num_of_players, int) or num_of_players < 2 or num_of_players > max_players:
        num_of_players = input(f"Enter the number of players (2 - {max_players}): ")
        if num_of_players.isdigit():
            num_of_players = int(num_of_players)
    
    return num_of_players

def game(points_to_win=50):
    players = get_players()
    players_scores = [0 for _ in range(players)]

    current_player_id = 0
    while max(players_scores) < points_to_win:
        for current_player_id in range(players):
            current_player_scores = 0
            while True:
                choose = input(f"Player {current_player_id + 1} turn.\n"
                            f"You have {players_scores[current_player_id]} points total. "
                            f"You can save {current_player_scores} points from this round.\n"
                            "Do you want to roll (Y/n)? ").lower()
                if choose not in ("", "n", "y"):
                    continue
                elif choose == "n":
                    break
                
                points = roll()
                if points == 1:
                    current_player_scores = 0
                    print("It is 1. You loose your points :(")
                    break
                else:
                    current_player_scores += points
                    print(f"You earn {points} points!")

            if current_player_scores:
                players_scores[current_player_id] += current_player_scores
                print(f"You saved {current_player_scores} points. "
                        f"You have {players_scores[current_player_id]} points total.")
            
            print()
            current_player_id += 1
            if current_player_id >= players:
                current_player_id = 0
    
    max_score = max(players_scores)
    
    players_won = []
    prev_player_id = -1
    while True:
        try:
            prev_player_id = players_scores.index(max_score, prev_player_id + 1)
            players_won.append(prev_player_id)
        except ValueError:
            break

    for player_won in players_won:
        print(f"Player {player_won + 1} won!")

    score_table_sorted = sorted(players_scores, reverse=True)
    for score in score_table_sorted:
        player_id = players_scores.index(score) + 1
        print(f"{score} points - player {player_id}")

game()