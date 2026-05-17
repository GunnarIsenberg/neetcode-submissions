class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        curLen = 0
        l = 0


        #Check that the len contains more than one value, and return then len of the string if not, covering cases 0 and 1.
        if len(s) < 1:
            return len(s)

        for r in range(len(s)):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1

            charSet.add(s[r])

            if (r+1) - l > curLen:
                curLen = r+1 - l
        
        return curLen

        

        