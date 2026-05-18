class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = 0
        tot = 1
        for i in nums: 
            if i != 0:
                tot *= i
            else:
                z += 1
        res = []
        if z > 1:
            return [0] * len(nums)
        if z == 1:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(tot)
            return res
        else:
            for num in nums:
                res.append(tot // num)
            return res
        
        return res