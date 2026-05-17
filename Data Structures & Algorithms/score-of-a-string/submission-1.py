class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1

        scr = 0
        while r < len(s):
            scr += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1
        return scr