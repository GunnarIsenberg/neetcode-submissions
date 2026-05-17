class Solution:
    def rob(self, nums: List[int]) -> int:
        robLeft, robRight = 0, 0

        for n in nums:
            temp = max(n + robLeft, robRight)
            robLeft = robRight
            robRight = temp
        return robRight
