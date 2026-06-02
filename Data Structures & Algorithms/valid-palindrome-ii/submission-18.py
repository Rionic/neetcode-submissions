class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True

        def isPalindrome(l, r):
            print(s[l:r+1])
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            left += 1
            right -= 1
        return True


        