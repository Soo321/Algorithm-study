class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                result = stack.pop()
                result += stack.pop()
                stack.append(result)
            elif token == "-":
                result = stack.pop()
                result = stack.pop() - result
                stack.append(result)
            elif token == "*":
                result = stack.pop()
                result *= stack.pop()
                stack.append(result)
            elif token == "/":
                result = stack.pop()
                result = int(stack.pop()/result)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
        