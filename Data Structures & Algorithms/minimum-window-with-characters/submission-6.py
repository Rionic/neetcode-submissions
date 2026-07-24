class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, minL, minR = 0, 0, 1001
        charMap = defaultdict(int)
        for c in t:
            charMap[c] += 1
        for r in range(len(s)):
            if s[r] in t:
                charMap[s[r]] -= 1

            while max(charMap.values()) == 0: # Found substring
                if r - l + 1 < minR - minL + 1:
                    minR, minL = r, l
                if s[l] in charMap:
                    charMap[s[l]] += 1
                l += 1
        if minR == 1001: return ""
        return s[minL: minR + 1]
            