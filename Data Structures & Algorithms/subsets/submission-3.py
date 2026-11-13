class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []

        self.helper(0, nums, res, comb)
        return res
    
    def helper(self, i, nums, res, comb):
        if i >= len(nums):
            res.append(comb.copy())
            return
        
        comb.append(nums[i])
        self.helper(i + 1, nums, res, comb)

        comb.pop()
        self.helper(i + 1, nums, res, comb)
    

        
        