class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = sorted(s)
        r = sorted(t)

        if l == r:
            return True
        return False