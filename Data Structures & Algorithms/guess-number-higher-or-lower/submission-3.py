# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        h = n
        l = 0

        while l <= h:
            m = (h + l) // 2
            match guess(m):
                case -1:
                    h = m - 1 
                case 0:
                    return m
                case 1: 
                    l = m + 1
