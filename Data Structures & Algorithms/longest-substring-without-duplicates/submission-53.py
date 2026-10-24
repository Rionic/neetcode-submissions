class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcdef c ghijklmnop
        chars = set()
        longest, l = 0, 0

        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                longest = max(longest, len(chars))
            else:
                while chars and s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])

        return longest

