class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        totIndex = rows * cols - 1

        l = 0
        r = totIndex

        while l <= r:
            m = (l + r) // 2 

            mList = m // cols
            mIndex = m % cols
            mVal=matrix[mList][mIndex]

            if mVal == target:
                return True
            elif mVal > target:
                r = m - 1
            else:
                l = m + 1
        return False

    
        