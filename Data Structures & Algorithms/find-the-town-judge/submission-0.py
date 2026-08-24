class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        itrust = {}
        youtrust = {}

        for p in range(1, n + 1):
            itrust[p], youtrust[p] = 0, 0

        for rel in trust:
            itrust[rel[0]] += 1
            youtrust[rel[1]] += 1

        for p in range(1, n+1):
            if itrust[p] == 0 and youtrust[p] == n - 1:
                return p

        return -1