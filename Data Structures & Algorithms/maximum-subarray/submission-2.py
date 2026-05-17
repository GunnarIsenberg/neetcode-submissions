class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        cur = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            cur = max(dp[i], cur)
        return cur        