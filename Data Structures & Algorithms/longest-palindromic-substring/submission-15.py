class Solution:
    def longestPalindrome(self, s: str) -> str:
        p, l, r = '', 0, 0

        def expand(s, l, r, p):
            l, r = l, r
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > len(p):
                    p = s[l:r + 1]
                l -= 1
                r += 1
            return p
        for i in range(len(s)):
            p = expand(s, i, i+1, p)
            p = expand(s, i, i, p)
        return p
                


        