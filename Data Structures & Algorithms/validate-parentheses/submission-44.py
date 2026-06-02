class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        matching = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in matching:
                if not st or matching[c] != st[-1]:
                    return False
                st.pop()
            else:
                st.append(c)
        return len(st) == 0