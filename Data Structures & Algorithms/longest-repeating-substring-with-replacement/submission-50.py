class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, best = 0, 0
        charMap = Counter()
        for r in range(len(s)):
            charMap[s[r]] += 1
            
            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            
            best = max(best, r - l + 1)

        return best