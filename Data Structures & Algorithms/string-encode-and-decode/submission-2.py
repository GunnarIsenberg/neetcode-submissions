class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            l = len(s)
            to_add = str(l) + "#" + s
            res = res + to_add
        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            sub = s[j + 1 : j + 1 + l]
            res.append(sub)
            i = j + 1 + l
        return res