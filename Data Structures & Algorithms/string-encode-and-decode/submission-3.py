class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = ""
        while i < len(s):
            if s[i] == "#":
                res.append(s[i+1: i+1+int(length)])
                i += 1 + int(length)
                length = ""
            else:
                length += s[i]
                i += 1
        return res
