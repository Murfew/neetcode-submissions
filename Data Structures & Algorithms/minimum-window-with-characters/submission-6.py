class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        tCounts = Counter(t)
        seen = defaultdict(int)
        need = len(tCounts)
        have = 0

        for r in range(len(s)):
            char = s[r]

            if char in tCounts:
                seen[char] += 1

                if seen[char] == tCounts[char]:
                    have += 1

            while have == need:
                res = s[l: r + 1] if not res or len(s[l: r+ 1]) < len(res) else res
                removing = s[l]
                if removing in seen:
                    seen[removing] -= 1

                    if seen[removing] < tCounts[removing]:
                        have -= 1
                
                l += 1

        return res