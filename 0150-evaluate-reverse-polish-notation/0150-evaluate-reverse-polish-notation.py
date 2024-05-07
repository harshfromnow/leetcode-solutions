class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                if token == '+':
                    t = t2 + t1
                elif token == '-':
                    t = t2 - t1
                elif token == '/':
                    t = int(t2 / t1)
                else:
                    t = t1 * t2
                stack.append(t)
            else:
                stack.append(int(token))
        return stack.pop()