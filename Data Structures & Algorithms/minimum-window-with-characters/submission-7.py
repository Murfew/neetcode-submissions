class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        tCount = Counter(t)
        seen = {}
        have = 0
        need = len(tCount)

        for r in range(len(s)):
            if s[r] in tCount:
                seen[s[r]] = seen.get(s[r], 0) + 1

                if seen[s[r]] == tCount[s[r]]:
                    have += 1

                while have == need:
                    res = s[l: r + 1] if not res or len(s[l: r + 1]) < len(res) else res
                    if s[l] in tCount:
                        seen[s[l]] -= 1

                        if seen[s[l]] < tCount[s[l]]:
                            have -= 1
                    
                    l += 1

        return res