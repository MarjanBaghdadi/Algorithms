#credit: NeetCode Youtbe Channel
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1 way
        return sorted(s) == sorted(t)
    
        #2nd way
        #return Counter(s) == Counter(t)
    
        #3rd way
        if len(s) != len(t):
            return False
        countS, countT = {} , {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #.get() function returns the value from a dic in Python and if it can not find the key it returns none instead of error 
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
        
