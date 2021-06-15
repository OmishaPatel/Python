def acronym():
    acronym_list = []
    user_input = input("Enter full name of an organization to get acronym: ").title()
    for letter in user_input:
        if letter.isupper():
            acronym_list.append(letter)
    return ''.join(acronym_list)
    
print(acronym())
