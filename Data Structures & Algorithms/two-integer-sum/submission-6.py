class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            need = target - v

            if need in seen:
                return [seen[need], i]
            
            else:
                seen[v] = i
        
        