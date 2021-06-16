def isPalindrome(str1):
        str1 = "".join(i.lower() for i in str1 if i.isalnum())
        i = 0
        j = len(str1) -1
        while i < j:
            if str1[i] != str1[j]:
                return False
            i+=1
            j-=1
        return True
str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"
print(isPalindrome(str1))
print(isPalindrome(str2))