class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = ''
        maxLen = 0
        for r in range(len(s)):
            while s[r] in substring:
                l += 1
                substring = substring[1:]
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
            substring += s[r]
            
        return maxLen

# 'abcdefdabcef'
#     l  r            
