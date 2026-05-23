class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        need = defaultdict(list)

        for i1, val1 in enumerate(nums):
            for i2, val2 in enumerate(nums):
                if i1 == i2:
                    continue
                
                complement = -(val1 + val2)
                need[complement].append((i1, i2))
        
        res = set()

        for i3, val3 in enumerate(nums):
            if val3 in need:
                for i1, i2 in need[val3]:
                    if i3 not in (i1, i2):
                        res.add(tuple(sorted((nums[i1], nums[i2], val3))))

        return [list(triplet) for triplet in res]