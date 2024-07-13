class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # creating Hashmap
        countS, countT = {},{}
        
        # filling Hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # 1 + default value 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
         
        # checking values in hashmap are same or not
        for c in countS:
            # ti compares complete key and value
            if countS[c] != countT.get(c,0):
                return False
            
        return True
            