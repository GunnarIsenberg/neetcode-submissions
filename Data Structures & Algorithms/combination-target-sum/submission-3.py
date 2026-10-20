class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curList, curTotal, index):
            if curTotal == target:
                res.append(curList.copy())
                return
            if curTotal > target or index >= len(nums):
                return

            curList.append(nums[index])

            dfs(curList, curTotal + nums[index], index)

            curList.pop()

            dfs(curList, curTotal, index + 1)

        dfs([], 0, 0)
        return res