class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, res = 0, ''
        charMap = defaultdict(int)
        for c in t:
            charMap[c] += 1
        for r in range(len(s)):
            if s[r] in t:
                charMap[s[r]] -= 1

            while max(charMap.values()) == 0: # Found substring
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]
                if s[l] in charMap:
                    charMap[s[l]] += 1
                l += 1

        return res
            