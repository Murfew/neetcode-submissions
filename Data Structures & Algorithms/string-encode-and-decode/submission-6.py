class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        start = 0
        while start < len(s):
            stop = start + 1

            while s[stop] != "#":
                stop += 1

            length = int(s[start:stop])
            
            res.append(s[stop + 1: stop + 1 + length])
            start = stop + 1 + length

        return res