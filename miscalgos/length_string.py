def length_string_iterative(str):
    count = 0
    for i in range(len(str)):
        count += 1
    return count

def length_string_recursive(str):
    if str == '':
        return 0
    return 1 + length_string_recursive(str[1:])

str1 = 'helloworld'

print(length_string_iterative(str1))
print(length_string_recursive(str1))