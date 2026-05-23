class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        need = {}

        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if i1 == i2:
                    continue
                i, j = nums[i1], nums[i2]
                complement = 0 - (i + j)

                if complement in need:
                    need[complement].append([i1, i2])
                else:
                    need[complement] = [[i1, i2]]


        res = set()
        
        for i3 in range(len(nums)):
            cur = []
            if nums[i3] not in need:
                continue
            bkt = need[nums[i3]]
            for lst in bkt:
                if i3 not in lst:
                    cur.append([lst[0], lst[1], i3])
            for lst in cur:
                actual = []
                for idx in lst:
                    actual.append(nums[idx])
                res.add(tuple(sorted(actual)))

            
        
        return list(res)