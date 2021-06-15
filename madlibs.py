#getting user's input
adj = input('Enter an adjective: ')
noun1 = input('Enter an Noun: ')
verb1 = input('Enter an Verb: ')
noun2 = input('Enter an Noun: ')
verb2 = input('Enter an Verb: ')

#concatenating the string with variables
madlib = f"For my birthday, my parents took me and my best friends to the Super {adj} Lanes to go bowling.\
 I love the bowling alley -- its so {noun1}! First, we all rented funny bowling {verb1} and changed into them.\
 We had to leave our {noun2} with the front desk. I thought we looked like a bunch of {verb2}."

print(madlib)
