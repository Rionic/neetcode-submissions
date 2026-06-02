class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) > 0 and ord(c) - stack[-1] in {1, 2}:
                stack.pop()
            else:
                stack.append(ord(c))
        print(stack)
        return not stack

        