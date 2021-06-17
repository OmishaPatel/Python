def longest_common_prefix(strs):
    ans =""
    if len(strs) == 0:
        return ans
    
        
    for i in range(len(strs[0])):
        letter = strs[0][i]
        for j in range(len(strs)):
           if strs[j][i] != letter:
               return ans
        ans = ans + letter
    return ans

strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))