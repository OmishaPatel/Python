str1 = "aacc"
str2 = "ccac"
#using replace method
def is_permutation(str1, str2):
    ht =dict()
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    if len(str1) != len(str2):
            return False
    for i in str1:
        if i in ht:
            ht[i] +=1
        else:
            ht[i] = 1
    for i in str2:
        if i in ht:
            ht[i] -=1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True
   
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
            