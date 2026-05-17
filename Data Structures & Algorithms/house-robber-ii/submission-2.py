class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robLeft1, robRight1 = 0, 0
        for n in nums[1:]:
            tmp = max(robLeft1 + n, robRight1)
            robLeft1 = robRight1
            robRight1 = tmp
        
        robLeft2, robRight2 = 0, 0 
        for n in nums[:-1]:
            tmp = max(robLeft2 + n, robRight2)
            robLeft2 = robRight2
            robRight2 = tmp
        
        return max(robRight2, robRight1)

        