class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 0
        curBest = 1
        
        seen = {s[0]}
        while r < len(s) - 1:
            r += 1

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            curBest = max(curBest, r - l + 1)
        return curBest