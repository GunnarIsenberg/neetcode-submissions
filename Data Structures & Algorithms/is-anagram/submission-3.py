class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        sSet = set()
        tSet = set()
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
            sSet.add(c)

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
            tSet.add(c)
        
        if sSet != tSet:
            return False
        for c in sSet:
            if sMap[c] != tMap[c]:
                return False
        for c in tSet:
            if c not in sSet:
                return False
        return True
        

        