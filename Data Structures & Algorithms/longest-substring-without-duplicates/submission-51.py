class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLen = 0, 0, 0

        charSet = set()

        while r < len(s):
            while r < len(s) and s[r] not in charSet:
                charSet.add(s[r])
                maxLen = max(len(charSet), maxLen)
                r += 1
            while r < len(s) and s[r] in charSet:
                charSet.remove(s[l])
                l += 1
        
        return maxLen