class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Read the length of upcoming string
        # Stop at '#'
        # Extract that many chars
        # Start where we ended

        res = []

        i = j = 0

        while i < len(s):

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])

            i = j = j + length + 1

        return res