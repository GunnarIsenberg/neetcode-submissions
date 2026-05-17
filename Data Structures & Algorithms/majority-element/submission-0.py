class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        buckets = {} 
        
        for num in nums:
            buckets[num] = buckets.get(num, 0) + 1
            if buckets[num] > len(nums) // 2:
                return num
        