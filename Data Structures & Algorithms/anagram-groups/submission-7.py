class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # Build distinct key
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1

            key = ",".join(map(str, freq))

            res[key].append(s)

        return list(res.values())