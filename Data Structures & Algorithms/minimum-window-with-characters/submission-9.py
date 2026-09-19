class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = Counter(t)
        window = {}
        need = len(tCounts)
        have = 0

        l = 0
        res = ""

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tCounts and window[s[r]] == tCounts[s[r]]:
                have += 1

            while have == need:
                res = s[l: r + 1] if not res or len(s[l: r + 1]) < len(res) else res
                window[s[l]] -= 1

                if s[l] in tCounts and window[s[l]] < tCounts[s[l]]:
                    have -= 1

                l += 1

        return res