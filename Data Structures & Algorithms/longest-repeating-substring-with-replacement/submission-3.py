class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            replacements = (r - l + 1) - max(list(counts.values()))
            if replacements > k:
                counts[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)

        return res