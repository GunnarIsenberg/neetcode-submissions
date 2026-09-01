class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = set()

        i = j = 0

        while i < len(nums1):
            seen.add(nums1[i])
            i += 1

        while j < len(nums2):
            if nums2[j] in seen:
                res.add(nums2[j])
            j += 1
        
        return list(res)
