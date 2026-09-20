class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen:
                res = max(res, len(seen))

                while s[r] in seen:
                    seen.pop(s[l])
                    l += 1
            
            seen[s[r]] = seen.get(s[r], 0) + 1

        return max(res, len(seen))