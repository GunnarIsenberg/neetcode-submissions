class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            can1 = nums[i]
            target = 0 - can1
            j, k = i + 1, len(nums) - 1

            while j < k:
                # Could be an issue here with duplicate values in indexes 1 and 2 - may need to check those
                canSum = sum([can1, nums[j], nums[k]])
                if canSum == 0:
                    res.append([can1, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif canSum > 0: 
                    k -= 1
                else:
                    j += 1
            
        return res