class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        n = len(s)
        # ababd
        def check(l, r):
            print(s[l], s[r], l, r)
            for i in range(n):
                if r < n and l >= 0 and s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    r -= 1
                    l += 1
                    print('inequal')
                    break
            return (r - l + 1, r, l)

        for i in range(n - 1):
            curLen, r, l = max(check(i, i), check(i, i+1))
            if curLen > len(longest):
                longest = s[l : r + 1]

        return longest

