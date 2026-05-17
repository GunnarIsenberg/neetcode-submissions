class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {i:[] for i in range(len(nums) + 1)}
        frequency = {}
        keySet = set()
        toReturn = []
        for num in nums:
            #Update frequency associated with this number
            if num not in frequency:
                frequency[num] = 0 
            frequency[num] += 1

            #If we don't already have an entry for this key - add one.
            if num not in keySet:
                keySet.add(num)

        #Using each key, insert the value associated with each 
        for key in keySet:
            curFrequency = frequency[key]
            buckets[curFrequency].append(key)

        for i in range(len(nums), 0, -1):
            if k > 0:
                curBucket = buckets[i]
                while curBucket and k > 0:
                    #Not efficient way to remove from a list, quickly becomes performance bottleneck
                    toReturn.append(curBucket[0])
                    curBucket.remove(curBucket[0])
                    k -= 1
            else:
                break

        
        return toReturn




            
        