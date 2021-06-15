def find_uppercase_iterative(str):
    for char in str:
        if char.isupper():
            return char
    return "No uppercase character found"

def find_uppercase_recursive(str, index = 0):
    if str[index].isupper():
        return str[index]
    if index == len(str) - 1:
        return "No Uppercase characters found"
    return find_uppercase_recursive(str, index+1)
str1 = "Hellowordl"
str2 = "helloWorld"
str3 = "helloworld"


print(find_uppercase_iterative(str1))
print(find_uppercase_iterative(str2))
print(find_uppercase_iterative(str3))

print(find_uppercase_recursive(str1))
print(find_uppercase_recursive(str2))
print(find_uppercase_recursive(str3))