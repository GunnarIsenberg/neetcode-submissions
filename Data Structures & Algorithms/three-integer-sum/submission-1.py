class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for i in range(len(nums) - 2):
            f = nums[i]
            i = i + 1
            j = (len(nums) - 1)

            while i < j:
                l = nums[i]
                r = nums[j]

                curSum = f + l + r

                if curSum == 0:
                    localTup = tuple([f, l, r])
                    if localTup not in res:
                        res.add(localTup)
                    i += 1
                elif curSum > 0:
                    j -= 1
                else:
                    i += 1

        return list(res)




    


