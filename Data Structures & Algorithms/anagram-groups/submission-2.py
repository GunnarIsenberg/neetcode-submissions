class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        added = set()
        res = []
        for i in range(len(strs)):
            curBkt = []
            s = strs[i]
            if s in added:
                continue
            added.add(s)
            curBkt.append(s)
            for j in range(i + 1, len(strs)):
                if self.isAnagram(s, strs[j]):
                    curBkt.append(strs[j])
                    added.add(strs[j])
            res.append(curBkt)
            curBkt = []

        return res

    def isAnagram(self, s, t) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
        
        for key in count.keys():
            if count[key] != 0:
                return False
        return True
        