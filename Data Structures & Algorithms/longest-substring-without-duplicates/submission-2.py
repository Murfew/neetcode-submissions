class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            char = s[r]

            while char in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(char)
            res = max(res, r - l + 1)

        return res