import random
import string

letters = string.ascii_letters
number = string.digits
symbols = string.punctuation
#function to get length of password from user
def get_password_length():
    while True:
        length = input("Please enter a single or double digit desired password length: ")
        try:
            length = int(length)
            return length
        except:
            print("Sorry That's Wrong. Please enter a number again to get password")
# function to get choices from user to add either letter, number or symbols to password
def password_choices():
    while True:
        want_numbers = input("Do you want numbers in your password (True or False)? ")
        want_letter = input("Do you want letters in your password (True or False)? ")
        want_symbols = input("Do you want symbols in your password (True or False)? ")
        try:
            #evaluating the string output and converting it to boolean
            want_numbers = eval(want_numbers.title())
            want_letter = eval(want_letter.title())
            want_symbols = eval(want_symbols.title())
            #returning the list with user's choices
            return [want_numbers, want_letter, want_symbols]
        except NameError:
            print("Please enter either True or False")
            print("Invalid entry will result in selecting the default value. Try again to regenerate")
        return [True, True, True]
#function to create a string of password from users choice
def user_choice_combination():
    user_choice_list = password_choices()
    password_string = ''
    if user_choice_list[0]== True:
        password_string+= number
    else:
        password_string = ''
    if user_choice_list[1]== True:
        password_string+= letters
    else:
        password_string = ''
    if user_choice_list[2] == True:
        password_string+= symbols
    else:
        password_string = ''
    return password_string
# function to generate random password based on user's length and user's inclusion of either letters, numbers or symbols
def password_generator():
    length = get_password_length()  
    total_password_list = user_choice_combination()
    #converting to list so we can use shuffle
    total_password_list = list(total_password_list)
    random.shuffle(total_password_list)
    random_password = random.choices(total_password_list, k=length)
    random_password = ''.join(random_password)
    return f"Your {length} digit password is {random_password}"

def main():
    password = password_generator()
    print(password)

while True:
    main()
    play_again = input("Do you want to generate random password again (Y/N) ? ").lower()
    if play_again == 'no' or play_again == 'nah' or play_again == 'n':
        break




    

