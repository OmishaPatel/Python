str1 = "the cow flys."
str2 = "flys. cow th"
#using replace method
def is_permutation(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char in str2:
            str2 = str2.replace(char, "")
    return len(str2) == 0
   
    count = 0
    for char in str1:
        if char not in str2:
            count +=1
    return count == 0
#using variable to keep count
def is_permutation1(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    if len(str1) != len(str2):
        return False
    count = 0
    for char in str1:
        if char not in str2:
            count +=1
    return count == 0

print(is_permutation(str1, str2))
            