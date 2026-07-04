class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = [] # holds [char, count] pairs
        # "ddbbcccbdaa", k = 3
        #     ^
        # s = [[d, 2]]
        # c = [e, 1]
        for c in s:
            if st and st[-1][0] == c: # repeat letter
                if st[-1][1] == k - 1: # k-length str -> remove
                    st.pop()
                else:
                    st[-1][1] += 1 # increment repeat char count
            else:
                st.append([c, 1]) # non-repeat letter
        res = ''

        for c, f in st:
            res += c*f

        return res
