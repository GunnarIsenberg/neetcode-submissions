class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(step):
            if rootMap.get(step):
                return rootMap[step]
            if step == n:
                return 1
            if step > n:
                return 0
            elif step < n:
                rootMap[step] = helper(step + 1) + helper(step + 2)
                return rootMap[step]
            
        rootMap = {}
        return helper(0)