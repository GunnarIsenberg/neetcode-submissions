class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        keySet = set()
        counts = {}
        for n in nums:
            if n not in keySet:
                keySet.add(n)
            counts[n] = counts.get(n, 0) + 1
        
        i = 0
        for key in keySet:
            j = counts[key]
            while j > 0:
                nums[i] = key
                i += 1
                j -= 1
            


        