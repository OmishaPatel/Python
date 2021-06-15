def word_count():
    user_input = input("How do you feel today: ")
    word_counter = 0
    found_word = False
    for i in range(0, len(user_input)):
        if user_input[i].isalpha() and found_word == False:
            found_word = True
            word_counter += 1
        elif user_input[i].isalpha() == False:
            found_word = False
    print(f"You told me how you feel in {word_counter} words!!")
   

word_count()