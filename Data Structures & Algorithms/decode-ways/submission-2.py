class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i < len(s) - 1:
                if int( s[i] + s[i + 1]) <= 26:
                    res += dfs(i + 2)
            cache[i] = res
            return res
        return dfs(0)