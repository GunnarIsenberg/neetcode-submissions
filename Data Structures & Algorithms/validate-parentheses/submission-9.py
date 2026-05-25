class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        cList = s.split()
        complement = {')' : '(', '}' : '{', ']' : '['}
        charStack = []

        for i, c in enumerate(s):
            if c not in complement.keys():
                charStack.append(c)
            else:
                if not charStack or complement[c] != charStack[-1]:
                    return False
                charStack.pop()
        return not charStack


            
        