class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        err = 0

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            if err > 0:
                return False
            else:
                if self.checkPalindrome(s[i + 1:j + 1]) or self.checkPalindrome(s[i: j]):
                    return True
                return False
        return True
            #now we're at a spot where either left, or right must proceed - so what determines that? Maybe we just run a sub check on both substring?  
        
    def checkPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j: 
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            return False
        return True