class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(x, y, index):
            if index == len(word):
                return True
            if (x < 0 or y < 0 or
                x >= rows or y >= cols or
                word[index] != board[x][y] or
                (x, y) in path):
                return False

            path.add((x, y))
            res = ( dfs(x + 1, y, index + 1) or
                    dfs(x - 1, y, index + 1) or
                    dfs(x, y + 1, index + 1) or
                    dfs(x, y - 1, index + 1))
            path.remove((x, y))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False