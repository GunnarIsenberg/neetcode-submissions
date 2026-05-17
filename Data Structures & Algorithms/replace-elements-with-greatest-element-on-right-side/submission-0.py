class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       
        #Handling edge cases
        if len(arr) <= 2:
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return [-1]
            if len(arr) == 2:
                return [arr[1], -1]

        gr = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                gr = arr[i]
                arr[i] = -1
            else:
                if arr[i] > gr:
                    arr[i], gr = gr, arr[i]
                else:
                    arr[i] = gr
        arr[-1] = -1

        return arr


                
            
        