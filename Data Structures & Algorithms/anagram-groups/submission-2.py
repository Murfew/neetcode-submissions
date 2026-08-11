class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}
        for i, s in enumerate(strs):
            chars = frozenset(Counter(s).items())
            if chars in seen:
                res[seen[chars]].append(s)
            else:
                seen[chars] = len(res)
                res.append([s])

        return res