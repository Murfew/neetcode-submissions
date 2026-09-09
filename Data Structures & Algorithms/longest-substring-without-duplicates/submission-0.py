class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        start, stop = 0, 0
        seen = set()
        while stop < len(s):
            while s[stop] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[stop])
            stop += 1
            longest = max(longest, len(seen))

        return longest