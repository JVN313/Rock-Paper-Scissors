import random

# Game Variables
playing = True
player_wins = 0
computer_wins = 0
draws = 0
games_played = 0
error_count = 0
options = ["ROCK","PAPER","SCISSORS"]
answer = options[random.randrange(0,3)]
user_input = input("Type Rock, Paper, Scissors, or Q to quit the game: ").upper()

# Game Functions
def player_win():
    global player_wins
    player_wins+=1
    print("You Won!")

def replay():
    global answer,user_input
    answer = options[random.randrange(0,3)]
    user_input = input("To play again type Rock, Paper, Scissors, or Q to quit the game: ").upper()

def score_board():
    global score_entry
    score_board_add = open("RPSscoreboard.txt","a")
    score_entry = input("ENTER YOUR NAME TO BE PLACED ON THE LEADERBOARDS: ").upper()
    if score_entry == "Q" or score_entry == "QUIT":
        quit()
    score_board_add.write(f"\n{score_entry} {str(player_wins)}W/{str(computer_wins)}L/{str(draws)}D")
    score_board_add.close()
    score_board_show = open("RPSscoreboard.txt","r")
    print(score_board_show.read())
    score_board_show.close()

def log_error():
    global score_entry
    log_error_add = open("ErrorLog.txt", "a")
    log_error_add.write(f"\nUser {score_entry} Had {str(error_count)} Errors During Their Play")

# Game Loop
while playing:
    if user_input == "Q" or user_input =="QUIT":
        playing = False
    elif user_input == options[1] and answer == options[0]:
        games_played+=1
        player_win()
        replay()
    elif user_input == options[0] and answer == options[2]:
        games_played+=1
        player_win()
        replay()
    elif user_input == options[2] and answer == options[1]:
        games_played+=1
        player_win()
        replay()
    elif user_input not in options:
        error_count+=1
        print("Invalid Input")
        replay()
    elif user_input==answer:
        games_played+=1
        draws+=1
        print("DRAW!")
        replay()
    else:
        games_played+=1
        computer_wins+=1
        print("Sorry You Lost :( ")
        replay()
    
print(f"You Won {player_wins} Time(s), Lost {computer_wins} Time(s), And Had {draws} Draw(s)!")
score_board()
log_error()
print("Thanks For Playing!")