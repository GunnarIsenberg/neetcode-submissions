class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def oddHelper(i):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        def evenHelper(i):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]
            

        for i in range(len(s)):
            evenWord, oddWord = evenHelper(i), oddHelper(i)
            if len(evenWord) > len(res):
                res = evenWord
            if len(oddWord) > len(res):
                res = oddWord

        return res