class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        l, r = 1, piles[-1]
        res = r

        while l <= r:
            m = l + (( r - l ) // 2)
            total_hours = sum(math.ceil(v / m) for v in piles )
            if total_hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        

        