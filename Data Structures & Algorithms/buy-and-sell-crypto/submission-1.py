class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Nested loop with pointer at i, and second at i : -1, N^2 - not optimal
        #Left, right pointer moving inward and comparing? 
        #Left, Left + 1 pointer, moving either forward depending on effect on purchase? 
        #Both proposed O(N) solutions are naieve greedy algorithms, and not exhaustive. 
        l, r = 0, 1
        res = 0

        while r < len(prices):
            val = prices[r] - prices[l]

            if prices[l] > prices[r]:
                l = r
            
            if val > res:
                res = val 

            r += 1

            
        
        return res
                