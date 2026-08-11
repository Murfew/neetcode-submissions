class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}
        for i, string in enumerate(strs):
            chars = "".join(sorted(string))
            if chars in seen:
                res[seen[chars]].append(string)
                continue

            seen[chars] = len(res)
            res.append([string])

        return res