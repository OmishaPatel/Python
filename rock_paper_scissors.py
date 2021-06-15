import random

def play_game():
    user = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print (f"Computer chose {computer}: ")
    if user == computer:
        return "It\'s a tie"

    if who_won(user, computer):
        return "Congrats, You Won!"

    return "Sorry You lost"

def who_won(player1, player2):
    # return true if player wins
    # r > s, s > p, p > r
    if(player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') \
        or (player1 == 'p' and player2 == 'r'):
        return True

print(play_game())