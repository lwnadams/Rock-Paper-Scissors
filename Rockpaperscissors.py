import random



user = input("Enter Rock, Paper or Scissors: ")
#valididity =

while user not in ["Rock", "rock", "Paper", "paper", "Scissors", "scissors"]:
    user = input("Invalid entry, enter Rock, Paper or Scissors: ")


options = ["Rock", "Paper", "Scissors"]
computer = random.choice(options)


print(computer)

def play_game(computer, win_status):
    if win_status == "won":
        print("Congratulations! Computer chooses " +computer+ ", you win!")
    elif win_status == "lost":
        print("Computer chose " +computer+ ", you lost!")
    elif win_status == "draw":
        print("Computer chose "+computer+", its a draw!")

if computer == "Rock":
    if user == "rock" or "Rock":
        play_game(computer, "draw")
    elif user == "Scissors" or "scissors":
        play_game(computer, "lost")
    elif user == "Paper" or "paper":
        play_game(computer, "won")

if computer == "Paper":
    if user == "rock" or "Rock":
        play_game(computer, "lost")
    elif user == "Scissors" or "scissors":
        play_game(computer, "won")
    elif user == "Paper" or "paper":
        play_game(computer, "draw")

if computer == "Scissors":
    if user == "rock" or "Rock":
        play_game(computer, "won")
    elif user == "Scissors" or "scissors":
        play_game(computer, "draw")
    elif user == "Paper" or "paper":
        play_game(computer, "lost")

    