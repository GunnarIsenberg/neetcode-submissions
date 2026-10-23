class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        l,r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum == target:
                return [l + 1, r + 1]
            
            if curSum > target:
                r -= 1
                continue
            
            if curSum < target:
                l += 1
                continue