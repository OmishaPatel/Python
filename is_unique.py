
# Using dictionary
def is_unique(str):
    d = dict()
    for char in str.strip():
        d[char] = d.get(char,0) + 1

    for key,value in d.items():
        if value > 1:
            return False
        return True

print(is_unique("true"))

#Using Set
def is_unique1(str):
    return len(str) == len(set(str))

print(is_unique("unique"))