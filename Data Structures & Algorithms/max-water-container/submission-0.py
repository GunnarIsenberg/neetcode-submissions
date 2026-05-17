class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curGuess = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            if curGuess < area:
                curGuess = area

            #What is the update logic? We can scan either independently 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return curGuess


                    