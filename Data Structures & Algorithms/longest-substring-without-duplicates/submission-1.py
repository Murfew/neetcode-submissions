class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        longest = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[i])
            longest = max(longest, len(seen))

        return longest