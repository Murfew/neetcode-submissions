class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue

            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))

        return stack[0]

                

            