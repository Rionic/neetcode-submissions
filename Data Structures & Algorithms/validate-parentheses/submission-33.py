class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for c in s:
            print(c,st)
            if c in ['(', '[', '{']:
                st.append(c)
            elif len(st) == 0:
                return False
            elif c == ']' and st[-1] == '[':
                st.pop()
            elif c == ')' and st[-1] == '(':
                st.pop()
            elif c == '}' and st[-1] == '{':
                st.pop()
            else:
                return False
        print(st)
        return len(st) == 0