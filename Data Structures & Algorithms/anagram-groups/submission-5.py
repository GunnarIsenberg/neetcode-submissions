class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            curMap = [0] * 26

            for c in s:
                curMap[ord(c) - ord("a")] += 1

            res[tuple(curMap)].append(s)
        return list(res.values())