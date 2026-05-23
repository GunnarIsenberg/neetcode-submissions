class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        for i, v in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if v + nums[l] + nums[r] < 0:
                    l += 1
                elif v + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.add(tuple(sorted([v, nums[l], nums[r]])))
                    r -= 1
                    l += 1
        
        return list(res)

        