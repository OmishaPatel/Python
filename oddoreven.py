def odd_even():
    while True:
        num = input("What number are you thinking? ")
        try:
            num = int(num)
            if num % 2 == 0:
                print("That's an even number!")
            else:
                print("That's an odd number!")
        except ValueError:
            print("Please enter a numerical number between 1 and 1000.")            
odd_even()
