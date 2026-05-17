class Solution:
    def climbStairs(self, n: int) -> int:
        #Map Root : answer
        rootMap = {}
        return self.calcSteps(rootMap, n, 0)
    
    def calcSteps(self, rootMap, target, step):
        if rootMap.get(step):
            return rootMap[step]
        elif step == target:
            return 1
        elif step > target:
            return 0
        elif step < target:
            rootMap[step] = self.calcSteps(rootMap, target, step + 1) + self.calcSteps(rootMap, target, step + 2)
            return rootMap[step]