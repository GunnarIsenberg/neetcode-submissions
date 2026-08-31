class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid[0]), len(grid)
        res = 0

        def helper(x, y, walk):
            if min(x, y) < 0 or x == ROWS or y == COLS or grid[y][x] == 1 or (x,y) in walk:
                return 0
            if (x, y) == (ROWS - 1, COLS - 1):
                return 1
            
            walk.add((x, y))
            
            count = 0
            count += helper(x + 1, y, walk)
            count += helper(x - 1, y, walk)
            count += helper(x, y + 1, walk)
            count += helper(x, y - 1, walk)
            
            walk.remove((x, y))

            return count

        return helper(0,0,set())