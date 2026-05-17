class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for b in range(len(prices)):
            buy = prices[b ]
            for s in range(b + 1, len(prices)):
                sell = prices[s]
                res = max(res, sell - buy)
        return res
        