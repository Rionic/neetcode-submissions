class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        charMap = Counter(t)
        missing = len(t)
        l, r = 0, 0
        bestL, bestR = 0, len(s) + 1

        while r < len(s):
            if charMap[s[r]] > 0:
                missing -= 1
            charMap[s[r]] -= 1
            r += 1

            while missing == 0:
                if r - l < bestR - bestL:
                    bestL, bestR = l, r
                charMap[s[l]] += 1
                if charMap[s[l]] > 0:
                    missing += 1
                l += 1
            
        return s[bestL:bestR] if bestR - bestL <= len(s) else ""