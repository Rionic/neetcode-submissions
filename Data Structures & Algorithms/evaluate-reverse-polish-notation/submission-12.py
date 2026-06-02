class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # n1=4, n2=9
        # 9 - 4 = 5
        import operator
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        stack = []

        for t in tokens:
            if t not in ['+', '-', '/', '*']:
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                print(n2, t, n1)
                res = int(ops[t](n2, n1))
                print(res)
                stack.append(res)
                print(stack)

        return stack.pop()
            