vowels = "aeiou"

def count_consonants(str):
    count = 0
    for char in str:
        if char.lower() not in vowels and char.isalpha():
            count += 1
    return count

def count_consonants_recursive(str):
    if str == '':
        return 0
    if str[0].lower() not in vowels and str[0].isalpha():
        return 1 + count_consonants_recursive(str[1:])
    return count_consonants_recursive(str[1:])
str1 = "abc de"
str2 = "hello world"

print(count_consonants(str1))
print(count_consonants(str2))
print(count_consonants_recursive(str1))
print(count_consonants_recursive(str2))