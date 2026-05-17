class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keySet = set()
        valMap = {}
        toReturn = []

        for i in range(len(strs)):
            curStr = strs[i]
            strKey = ""
            for c in sorted(curStr):
                strKey += c

            if strKey in valMap:
                valMap[strKey].append(strs[i])
            else:
                keySet.add(strKey)
                valMap[strKey] = [strs[i]]
            
        for key in keySet:
            toReturn.append(valMap[key])


        return toReturn
        