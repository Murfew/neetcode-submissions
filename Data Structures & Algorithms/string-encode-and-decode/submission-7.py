class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = j = 0
        while i < len(s):

            if s[j] != "#":
                j += 1
                continue

            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            j = i

            
        return res
