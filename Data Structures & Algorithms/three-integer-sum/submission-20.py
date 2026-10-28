class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, n in enumerate(nums):

            if i > len(nums) - 3:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                curSum = sum([n, nums[j], nums[k]])

                if curSum == 0:
                    res.add((n, nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif curSum > 0:
                    k -= 1

                else:
                    j += 1
            
        return [list(t) for t in res]