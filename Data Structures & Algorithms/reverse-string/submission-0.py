class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        q = []
        for c in s:
            q.append(c)
        
        for i in range(len(s)):
            s[i] = q.pop()

        