class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
    
        Map1,Map2 = {},{}

        for i in range(len(s)):
            Map1[s[i]] = Map1.get(s[i],0)  + 1
            Map2[t[i]] = Map2.get(t[i],0)  + 1

        return Map1 == Map2