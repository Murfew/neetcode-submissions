class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = {}

        for s in strs:
            chars_list = [0] * 26
            for c in s:
                chars_list[ord(c) - ord("a")] += 1

            chars = ",".join(map(str, chars_list))

            if chars in seen:
                res[seen[chars]].append(s)
                continue
            
            res.append([s])
            seen[chars] = len(res) - 1 


        return res