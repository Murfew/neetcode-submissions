class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
                continue

            if bracket in [")", "}", "]"]:
                if not stack:
                    return False
                
                if bracket == ")":
                    last = stack.pop()
                    if last != "(":
                        return False
                    
                    continue

                if bracket == "]":
                    last = stack.pop()
                    if last != "[":
                        return False
                    
                    continue

                if bracket == "}":
                    last = stack.pop()
                    if last != "{":
                        return False
                    
                    continue

        return len(stack) == 0
            


