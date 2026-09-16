class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        tCounts = Counter(t)
        seen = defaultdict(int)
        have = 0
        need = len(tCounts)
        l = 0

        for r in range(len(s)):
            if s[r] in tCounts:

                seen[s[r]] += 1

                if seen[s[r]] == tCounts[s[r]]:
                    have += 1

                while have == need:
                    res = s[l: r + 1] if not res or len(s[l: r + 1]) < len(res) else res

                    if s[l] in tCounts:
                        seen[s[l]] -= 1

                        if seen[s[l]] < tCounts[s[l]]:
                            have -= 1

                    l += 1
            

        return res