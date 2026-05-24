class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        res = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            bktArea = min(lh, rh) * (r - l)        
            res = max(res, bktArea)

            if lh > rh:
                r -= 1
            elif lh <= rh:
                l += 1
        
        return res

