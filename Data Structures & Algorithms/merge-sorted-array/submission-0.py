class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        for num in nums2:
            nums1[i] = num 
            i += 1
        
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            else:
                m = len(arr) // 2
                left = mergesort(arr[m:])
                right = mergesort(arr[:m])
                return merge2(left, right)

             
        def merge2(arr1, arr2):
            i, j = 0, 0
            res = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
                
            if i < len(arr1):
                res += arr1[i:]
            if j < len(arr2):
                res += arr2[j:]
            return res

        nums1[:] = mergesort(nums1)
              