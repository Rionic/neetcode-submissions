class Solution:
    def partition(self, s: str) -> List[List[str]]:

        substrings = []

        def partition(l, pals):
            # print(pals)
            if l == len(s):
                substrings.append(pals.copy())

            for r in range(l + 1, len(s) + 1): # +1?
                if s[l:r] == s[l:r][::-1]:
                    pals.append(s[l:r]) # no copy issue apaprently
                    partition(r, pals)
                    pals.pop()


        partition(0, [])
        return substrings