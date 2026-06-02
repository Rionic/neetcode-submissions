class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r , longest = 0, 0, 0
        charSet = set()
        # asdfskqlcp
        # l   r
        # asdf

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
            