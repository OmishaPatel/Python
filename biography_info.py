import datetime
def biography_info():
    while True:
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Please enter a valid name")
        else:
            break
    while True:
        date_of_birth = input("Enter Your Date of Birth in the format DD/MM/YYYY: ")
        try:
            datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
            break
        except ValueError:
            print("Please enter valid date of birth in the format DD/MM/YYYY")
            
    
    address = input("Enter your address: ")   
    personal_goals = input("Please enter your personal goals: ")
    print(f"- Name: {name}\n- Address: {address}\n- Date Of Birth: {date_of_birth}\n- Personal Goals: {personal_goals}")


biography_info()