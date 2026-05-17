class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def bfs(r, c, visit):
            q = collections.deque()
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                cur_r, cur_c = q.popleft()
                visit.add((cur_r, cur_c))
                for cr, cc in directions:
                    nr, nc = cur_r + cr, cur_c + cc
                    if(0<=nr<rows and 0<=nc<cols 
                    and (nr, nc) not in visit and
                    heights[nr][nc] >= heights[cur_r][cur_c]):
                        q.append((nr, nc))

        for r in range(rows):
            bfs(r, 0, pac)
            bfs(r, cols - 1, atl)

        for c in range(cols):
            bfs(0, c, pac)
            bfs(rows - 1, c, atl)

        res = []
        for pair in pac:
            if pair in atl:
                res.append(pair)
        return res

    
        