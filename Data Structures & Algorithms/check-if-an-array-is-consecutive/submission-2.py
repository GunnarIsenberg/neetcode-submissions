class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0] - 1

        for num in nums:
            if num != prev + 1:
                return False
            prev += 1
        return True
