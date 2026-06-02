class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen = 0, 0
        charSet = []

        for r in range(len(s)):

            while s[r] in charSet:
                del charSet[0]
                l += 1
            
            charSet.append(s[r])
            maxLen = max(maxLen, len(charSet))

        return maxLen