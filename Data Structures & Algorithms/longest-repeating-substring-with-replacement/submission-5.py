class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1

            replacements = sum(list(counts.values())) - max(list(counts.values()))

            while replacements > k:
                counts[s[l]] -= 1
                l += 1

                replacements = sum(list(counts.values())) - max(list(counts.values()))

            res = max(res, r - l + 1)

        return res