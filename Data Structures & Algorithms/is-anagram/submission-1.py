class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        scounter = {}
        tcounter = {}

        for i in range(len(s)):
            scounter[s[i]] = 1 + scounter.get(s[i], 0)
            tcounter[t[i]] = 1 + tcounter.get(t[i], 0)

        return scounter == tcounter


            
        
        