import random
def rolling_dice():
    while True:
        num = input("Do you want to roll a dice? (Please enter yes or no): ").strip().lower()
        try:
            if num == "yes":
                pass
            elif num == "no":
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Please enter either yes or no to continue the game.")
            continue
        dice_num = random.randint(1,6)
        print(f"Your dice number is : {dice_num}")

rolling_dice()
