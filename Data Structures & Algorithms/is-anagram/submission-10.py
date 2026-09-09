class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapOne = {}
        mapTwo = {}
        i = 0
        while i < len(s):
            mapOne[s[i]] = mapOne.get(s[i], 0) + 1
            mapTwo[t[i]] = mapTwo.get(t[i], 0) + 1
            i += 1
        
        if mapOne == mapTwo:
            return True

        return False
