class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            if tuple(sorted(Counter(s).items())) not in res:
                res[tuple(sorted(Counter(s).items()))] = [s]
            else:
                res[tuple(sorted(Counter(s).items()))].append(s)
        return list(res.values())