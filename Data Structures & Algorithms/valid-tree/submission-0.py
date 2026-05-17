class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        tree = {i : [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        visited = set()

        def dfs(val, prev):
            if val in visited:
                return False
            visited.add(val)
            for v in tree[val]:
                if v == prev:
                    continue
                if not dfs(v, val):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

        
        