def look_and_say(n):
    
    s = "1"
    for i in range(n-1):
        s = next_number(s)
    return s

def next_number(s):
    i = 0
    result = ""
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i]==s[i+1]:
            count +=1
            i +=1
        result += str(count)+s[i]
        i += 1
    return result
print(look_and_say(0))