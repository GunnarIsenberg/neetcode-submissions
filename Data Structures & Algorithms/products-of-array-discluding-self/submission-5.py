class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        #I know that any value may be 0

        #If 0 is in the set of values excluding our current pointer
        # // 0 -> crash

        
        # * 0 -> return 0 

        #Since there can be two zeroes, in that case -> every value must return 0. 
        #Counter outside of the loop? 

        #Three cases:
        #1) No Zeroes - no special handling DONE
        #2) One Zeroe - in which case only the index of that zero should return a non zero integer
        #3) Two+ Zeroes - in this case, we always expect 0 DONE

        #Iterate over the nums list, count zeroes, build a switch case to map the function? 


        #TODO: We still fail a single zero case
        numZeroes = 0
        common_val = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                numZeroes += 1
                continue
            common_val = common_val * nums[i]
        
        #Reducing numZeroes to a max of 2 to match switch case syntax
        if numZeroes > 2:
            numZeroes = 2
            
        match numZeroes:
            case 0:
                for i in range(len(nums)):
                    results.append(common_val // nums[i])
            case 1:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        results.append(common_val)
                    else:
                        results.append(0)
            case 2: 
                for i in range(len(nums)):
                    results.append(0)
        
        return results
