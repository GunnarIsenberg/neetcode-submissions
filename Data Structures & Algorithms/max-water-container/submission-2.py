class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while r > l: 
            vol = min(heights[r], heights[l]) * (r - l)
            if vol > res:
                res = vol
            
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1

        return res

        