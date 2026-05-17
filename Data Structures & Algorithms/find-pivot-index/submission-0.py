class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        for i in range(1, len(nums)):
            right_sum += nums[i]

        left_sum = 0
        for i in range(0, len(nums)):
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
                if i + 1 >= len(nums):
                    return -1
                right_sum -= nums[i + 1]
            
