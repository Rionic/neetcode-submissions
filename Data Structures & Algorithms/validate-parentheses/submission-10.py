class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            # if len(stack) == 0:
            #     stack.append(b)
            if stack and ord(b) - ord(stack[-1]) in (1, 2):
                stack.pop()
            else:
                stack.append(b)
        return not stack
        