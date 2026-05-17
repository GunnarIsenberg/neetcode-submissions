class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        b, s = 0, 1

        while s < len(prices):
            res = max(prices[s] - prices[b], res)
            if prices[s] < prices[b]:
                b = s
            s += 1
        return res
