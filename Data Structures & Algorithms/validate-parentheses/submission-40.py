class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        matching = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in matching:
                if len(st) > 0 and matching[c] == st[-1]:
                    print('ya')
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return len(st) == 0