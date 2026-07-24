class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        l, m = 0, 0
        # "zxyzxyz"
        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[r])
            m = max(m, len(cs))
        
        return m
