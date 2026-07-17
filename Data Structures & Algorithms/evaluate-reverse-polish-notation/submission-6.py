class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in {"+", "-", "*", "/"}:
                stack.append(int(tokens[i]))
            else:
                num0 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(num0+num1)
                elif tokens[i] == '-':
                    stack.append(num1-num0)
                elif tokens[i] == '*':
                    stack.append(num0*num1)
                elif tokens[i] == '/':
                    stack.append(int(num1/num0))
        return stack[0]