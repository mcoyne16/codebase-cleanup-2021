
from random import choice

def determine_winner(p1, p2):
    pass    



if __name__ == '__main__':
    #
    # USER SELECTION
    #

    Valid_Options = ["rock", "paper", "scissors"]

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in Valid_Options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(Valid_Options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    # code attributed to shared solution from Kevin Pinkerton, Wednesday, Feb 2 in Slack
    wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
    if (u, c) in wins:
        print("You win!")
    elif u == c:
        print("You tied.")
    else:
        print("You lose.") 