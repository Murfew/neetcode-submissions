import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for t in tokens:
            if t in ops:
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(ops[t](num1, num2)))

            else:
                stack.append(int(t))

        return stack[0]
