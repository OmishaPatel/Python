def tip_calculator():
    while True:
        total = input("Please enter total amount of your bill: ")
        try:
            total = float(total)
            break
        except ValueError:
            print("Please enter numeric numbers for your total bill. ")
    tip_18 = round(total * 0.18, 2)
    tip_20 = round(total * 0.20, 2)
    tip_25 = round(total * 0.25, 2)
    total_with_tip_18 = round(tip_18 + total, 2)
    total_with_tip_20 = round(tip_20 + total, 2)
    total_with_tip_25 = round(tip_25 + total, 2)
    print(f"18% tip is {tip_18}, which brings your total to {total_with_tip_18}")
    print(f"18% tip is {tip_20}, which brings your total to {total_with_tip_20}")
    print(f"18% tip is {tip_25}, which brings your total to {total_with_tip_25}")
    while True:
        num_of_people = input("How many people are sharing the bill? ")
        try:
            num_of_people = int(num_of_people)
            break
        except ValueError:
            print("Please enter either single or double digit numeric number. ")
    print(f"With 18% percent tip each person will evenly have to pay {round(total_with_tip_18/num_of_people, 2)}.")
    print(f"With 20% percent tip each person will evenly have to pay {round(total_with_tip_20/num_of_people, 2)}.")
    print(f"With 25% percent tip each person will evenly have to pay {round(total_with_tip_25/num_of_people, 2)}.")

tip_calculator()