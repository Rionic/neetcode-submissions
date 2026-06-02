class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r, maxL, maxR = 0, 0, 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxR - maxL + 1:
                    maxL, maxR = l, r
                r += 1
                l -= 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxR - maxL + 1:
                    maxL, maxR = l, r
                r += 1
                l -= 1

        return s[maxL:maxR + 1]