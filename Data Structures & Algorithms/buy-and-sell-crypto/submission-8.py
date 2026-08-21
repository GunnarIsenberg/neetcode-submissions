class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        cur = 0

        l, r = 0, 1

        while r < len(prices):

            if prices[r] < prices[l]:
                l, r = r, r + 1
                if r >= len(prices):
                    break

            curProfit = prices[r] - prices[l]
            cur = max(curProfit, cur)
            r += 1

        return cur

        