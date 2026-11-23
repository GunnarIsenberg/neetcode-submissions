class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for c in s:
            charMap[c] = charMap.get(c, 0) + 1
        
        for c in t:
            charMap[c] = charMap.get(c, 0) - 1

        for key in charMap.keys():
            if charMap[key] != 0:
                return False
        return True

        