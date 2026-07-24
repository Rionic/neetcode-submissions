class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        l, minL, minR = 0, 0, 1001
        charMap = defaultdict(int)
        for c in t:
            charMap[c] += 1
        # X: 0
        # Y: 0
        # Z: 0
        # t="XYZ"
        # s="OUZODYXAZV"
        #          r
        #    l
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
            