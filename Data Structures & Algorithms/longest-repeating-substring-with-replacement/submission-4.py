class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        seen = defaultdict(int)

        for r in range(len(s)):
            seen[s[r]] += 1

            currLen = r - l + 1
            maxFreq = max(list(seen.values()))
            replacements = currLen - maxFreq
            while replacements > k:
                seen[s[l]] -= 1
                l += 1

                currLen = r - l + 1
                maxFreq = max(list(seen.values()))
                replacements = currLen - maxFreq

            res = max(res, currLen)

        return res