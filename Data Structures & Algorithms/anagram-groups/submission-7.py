class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i, string in enumerate(strs):
            sorted_str = "".join(sorted(string))
            anagrams[sorted_str].append(string)
        
        res = []
        for key in anagrams.keys():
            res.append(anagrams[key])
        
        return res

        