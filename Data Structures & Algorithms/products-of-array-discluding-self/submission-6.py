class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1

        for i in nums: tot *= i
        
        res = [(tot // i) if i != 0 else math.prod(nums[:j] + nums[j+1:]) for j, i in enumerate(nums)]
        return res