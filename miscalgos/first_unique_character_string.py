def firstUniqChar(s):
        for char in s:
            if s.count(char) == 1:
                return s.find(char)
        return -1 
str1 = "loveleetcode"
str2 = "aabb"
print(firstUniqChar(str1))
print(firstUniqChar(str2))