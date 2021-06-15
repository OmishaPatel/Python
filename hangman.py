import random
from hangman_visual import count_visual_dict
word_list = [ 'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw']

# function to return how many times the word has the same letter which is equal to guess
def how_many_times(word,guess):
    a = 0
    for char in word:
        if char == guess:
            a+=1
    return a 

word = random.choice(word_list).lower()
user_name = input("What's Your Name: ")
print(f"Welcome to hangman game. Good luck {user_name}")
print("Start guessing letters...")
# to keep a track of characters entered by user
guesses = []
# number of chances the user has
count = 7

while count > 0 and guesses != word :
    #printing the current word
    word_to_guess = [char if char in guesses else '-' for char in word]
    print('Current Word: ', ' '.join(word_to_guess))
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You already guessed that")
        continue
    if guess in word and guess != '':
        print(f"You guessed the letter {guess} right")
        b = how_many_times(word,guess)
        for i in range(0,b):
            # here appending the number of times the letter repeats in word
            guesses.append(guess)
        if len(guesses) == len(word):
            print(f"Congrats! You guessed the word {word} correctly!")
            break
        else:
            guessLeft = len(word) - len(guesses)
            print(f"You have {guessLeft} letters left to guess!")
    else:
        count -=1
        if count == 0:
            print(count_visual_dict[count])
            print("Sorry You lost!")
        else:
            print(count_visual_dict[count])
            print(f"Wrong guess. You have {count} lives left.")


    


    
