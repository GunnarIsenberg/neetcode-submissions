class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            arr1 = mergesort(arr[:mid])
            arr2 = mergesort(arr[mid:])

            return merge(arr1, arr2)

        def merge(a1, a2):
            res = []
            l = 0
            r = 0

            while l < len(a1) and r < len(a2):
                if a1[l] >= a2[r]:
                    res.append(a1[l])
                    l += 1
                else:
                    res.append(a2[r])
                    r += 1

            res.extend(a1[l:])
            res.extend(a2[r:])   

            return res             
 
        return mergesort(nums)[::-1]

        