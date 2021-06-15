import random

#function to make user guess a number thats randomly selected by python from a range
def user_guess_number(n):
    random_number = random.randint(1, n) # to get the random number from the random package
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < random_number:
            print("Sorry guess again. Too low.")
        elif guess > random_number:
            print("Sorry guess again. Too high. ")
        
    print(f"Congrats, you have guessed right {random_number} correctly.")

user_guess_number(10)

#function to make python guess what number the user typed

def python_guess(n):
    low = 1
    high = n
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could be high as low == high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f"Python has guessed your {guess} number, correctly!")

python_guess(500)


