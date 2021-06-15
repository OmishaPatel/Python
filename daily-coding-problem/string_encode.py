def encode(s):
    count = 0
    seen = ""
    result = ""
    for i in range(len(s)):
        if seen == s[i]:
            count+=1
        else:
            result += str(count) + seen
            seen = s[i]
            count = 1
    # updating  the last count to result
    result += str(count) + seen
    # removing 0 at the front of the string
    return result[1:]
    


def decode(s):
    result = ''
    count = 0
    for char in s:
        if char.isdigit():
            count = int(char)

        else:
            result += char * count
            count = 0
    return result





print(encode("AAAABBBCCDDAA"))
print(decode("4A3B2C2D2A"))
