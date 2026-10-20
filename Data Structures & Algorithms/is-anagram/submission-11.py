class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}

        for c in s:
            map1[c] = map1.get(c, 0) + 1
        
        for c in t:
            map2[c] = map2.get(c, 0) + 1
        
        if map1.keys() != map2.keys():
            return False
        
        for key in map1.keys():
            if map1[key] != map2[key]:
                return False

        return True
