class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while j < len(s):
            if i == len(t):
                return False
            
            if s[j] == t[i]:
                j += 1

            i += 1
        
        return True