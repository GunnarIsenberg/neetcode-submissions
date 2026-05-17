class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        j = 0
        while j <= 31:
            if n & 1:
                res += 1
            n = n >> 1
            j += 1

        return res