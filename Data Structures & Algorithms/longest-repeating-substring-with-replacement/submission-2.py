class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1

            currLength = r - l + 1
            replacements = currLength - max(list(counts.values()))

            if replacements <= k:
                res = max(res, currLength)
            else:
                counts[s[l]] -= 1
                l += 1

        return res