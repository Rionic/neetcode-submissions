class Solution:
    def isValid(self, s: str) -> bool:
        bm = {')': '(', '}': '{', ']': '['}
        st = []
        for b in s:
            if b in bm.keys(): #closing
                if not st or st[-1] != bm[b]:
                    return False
                else:
                    st.pop()
            else:
                st.append(b)
        
        return len(st) == 0