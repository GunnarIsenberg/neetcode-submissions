class Solution:
    def countBits(self, n: int) -> List[int]:

            
        def helper(k):
            count = 0
            while k > 0:
                if k & 1:
                    count += 1
                k = k >> 1
            return count

        res = [0] * (n + 1)
        for i in range(n + 1):
            count = helper(i)
            res[i] = count
        return res
        