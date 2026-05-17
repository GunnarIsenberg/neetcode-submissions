class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ptr = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= ptr:
                ptr = i
        return True if ptr == 0 else False
            
        