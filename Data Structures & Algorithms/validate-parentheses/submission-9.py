class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            print(ord(b))
            if len(stack) == 0:
                stack.append(b)
            elif ord(b) - ord(stack[-1]) in (1, 2):
                print('a')
                stack.pop()
            else:
                stack.append(b)
        print(stack)
        return not stack
        