class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        counter = res = None

        for num in nums:
            counter = (counter + num) if counter is not None else num
            res = max(counter, res) if res is not None else counter
        
        counter = None
        for num in reversed(nums):
            counter = (counter + num) if counter is not None else num
            res = max(counter, res) if res is not None else counter
        
        return res



