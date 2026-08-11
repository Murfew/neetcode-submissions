class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}
        for i, s in enumerate(strs):
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1

            count = tuple(count)

            if count in seen:
                res[seen[count]].append(s)
            else:
                seen[count] = len(res)
                res.append([s])


        return res