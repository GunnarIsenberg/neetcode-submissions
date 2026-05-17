class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        if sMap.keys() != tMap.keys():
            return False
            
        else:
            for key in sMap.keys():
                if sMap[key] != tMap[key]:
                    return False
        return True