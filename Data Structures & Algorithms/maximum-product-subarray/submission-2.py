class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            curMin, curMax = min(curMin * n, curMax * n, n), max(curMax * n, curMin * n, n)
            res = max(curMax, res)
        return res


        
        