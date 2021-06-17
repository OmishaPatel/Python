class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        s = self.countAndSay(n-1)
        return self.say(s)
    def say(self,s):
        result = ''
        count = 0
            
        if len(s) == 1:#base case when n is 1
            return "11"
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                count +=1
                result += str(count)
                result += str(s[i-1])
                #resetting count to 0 after adding prev element with its count to answer
                count = 0
                    
                    
        if s[-1] == s[-2]: # check last character same as prev element
            count += 1
            result += str(count)
            result += str(s[-1])
        else:
            result += str(1)# since there could be only 1 count for last unique element
            result += str(s[-1])
                
        return result
# time complexity O(m*n)