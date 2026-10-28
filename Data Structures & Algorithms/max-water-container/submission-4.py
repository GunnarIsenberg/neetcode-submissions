class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        canVol = 0

        while l < r: 
            lftHeight, rtHeight = heights[l], heights[r]

            curVol = min(lftHeight, rtHeight) * (r - l)
            canVol = max(canVol, curVol)

            if lftHeight >= rtHeight:
                r -= 1
            elif lftHeight < rtHeight:
                l += 1


        return canVol
