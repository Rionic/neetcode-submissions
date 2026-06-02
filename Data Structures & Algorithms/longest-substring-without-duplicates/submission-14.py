class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = ''
        maxLen = 0
        for r in range(len(s)):
            # print('sub', substring)
            while s[r] in substring:
                    l += 1
                    substring = substring[1:]
            substring += s[r]
            if r - l + 1 > maxLen:
                    maxLen = r - l +1
            
        return maxLen

# 'abcdefdabcef'
#     l  r            
