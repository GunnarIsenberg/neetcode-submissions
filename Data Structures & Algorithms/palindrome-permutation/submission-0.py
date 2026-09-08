class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charMap = {}
        for c in s:
            charMap[c] = charMap.get(c, 0) + 1
        
        numOdd = 0
        for key in charMap.keys():
            if charMap[key] % 2 == 1:
                numOdd += 1
                if numOdd > 1:
                    return False
        return True
 
        