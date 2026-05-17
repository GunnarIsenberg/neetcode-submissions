class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strLens = [len(i) for i in strs]
        if min(strLens) <= 0:
            return ""
         
        res = ""
        l = 0
        while l < min(strLens):
            c = strs[0][l]

            for s in strs[1:]:
                if s[l] != c:
                    return res

            res = res + c
            l += 1

        return res

        