class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        
        cur_depth = 1
        res = 0

        while n >= cur_depth:
            n -= cur_depth
            cur_depth += 1
            res += 1
        
        return res