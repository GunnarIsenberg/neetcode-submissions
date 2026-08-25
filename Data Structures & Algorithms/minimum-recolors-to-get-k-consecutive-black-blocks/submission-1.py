class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, k - 1

        cur = 0

        for c in range(k):
            if blocks[c] == "W":
                cur += 1

        res = cur

        while j < len(blocks) - 1:
            if blocks[i] == "W":
                cur -= 1
            i, j = i + 1, j + 1

            if blocks[j] == "W":
                cur += 1

            res = min(cur, res)
        return res
    

        