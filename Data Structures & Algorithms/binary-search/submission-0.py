class Solution:
    def search(self, nums: List[int], target: int) -> int:    
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                 return m
        return -1
        