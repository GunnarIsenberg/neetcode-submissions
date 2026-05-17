class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        intSet = set()
        l = 0
        for i in range(len(nums)):
            if nums[i] not in intSet:
                intSet.add(nums[i])
                nums[l] = nums[i]
                l += 1
        return l