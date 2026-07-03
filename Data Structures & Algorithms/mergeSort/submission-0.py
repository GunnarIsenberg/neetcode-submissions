# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2
        
        srtd_left = self.mergeSort(pairs[:mid])
        srtd_right = self.mergeSort(pairs[mid:])

        return self.merge(srtd_left, srtd_right)

    def merge(self, l1, l2):
        i = j = 0
        res = []
        while i < len(l1) and j < len(l2):
            if l1[i].key <= l2[j].key:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while i < len(l1):
            res.append(l1[i])
            i += 1
        while j < len(l2):
            res.append(l2[j])
            j += 1
        return res
