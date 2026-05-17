class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        slen = len(s)
        if not s:
            return True
        for char in t:
            if s[sp] == char:
                sp += 1
            if sp==slen:
                return True
        return False