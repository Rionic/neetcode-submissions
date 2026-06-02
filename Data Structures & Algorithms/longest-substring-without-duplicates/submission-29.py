class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen = 0, 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
            charSet.add(s[r])

        return maxLen

# 'abcdefdabcef'
#     l  r            
