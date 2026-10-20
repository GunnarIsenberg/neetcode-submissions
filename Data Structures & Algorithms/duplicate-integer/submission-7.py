class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        itemSet = set()

        for num in nums:
            if num in itemSet:
                return True
            itemSet.add(num)
        return False
        