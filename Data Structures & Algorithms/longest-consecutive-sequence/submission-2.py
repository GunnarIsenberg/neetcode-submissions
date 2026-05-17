class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet =set(nums)
        res = 0

        for n in nSet:
            cur = 0
            if n - 1 not in nSet:
                cur += 1
            while n + 1 in nSet:
                cur += 1
                n += 1
            if cur > res:
                res = cur
        return res
        
        