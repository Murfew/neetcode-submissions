class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1

        while r < len(s2):
            substring = s2[l:r + 1]

            if Counter(s1) == Counter(substring):
                return True

            l += 1
            r += 1

        return False