class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
                continue
            else:
                res.append(tmp)
                tmp = 0
        res.append(tmp)

        return max(res)
            