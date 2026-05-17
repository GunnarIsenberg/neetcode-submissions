class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s2 = ""
        for char in s:
            if char.isalnum():
                s2 += char
            


        i = 0
        j = len(s2) - 1

        if len(s2) == 1 or 0:
            return True

        while i <= j:
            if s2[i] != s2[j]:
                return False
            i += 1
            j -= 1
            
        return True
        