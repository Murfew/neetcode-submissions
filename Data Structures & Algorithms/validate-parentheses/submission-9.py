class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for b in s:
            if b in pairs:
                stack.append(b)
            else :
                if not stack:
                    return False

                top = stack.pop()

                if b != pairs[top]:
                    return False

        return len(stack) == 0

