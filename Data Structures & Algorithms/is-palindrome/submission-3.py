class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        res = ''.join(c for c in s if c.isalnum())
        print(res)

        return res == res[::-1]