class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m, l = 0, 0
        charFreq = defaultdict(int)

        for r in range(len(s)):

            charFreq[s[r]] += 1
            # Max of fixed-size (max 26) array -> O(1)
            while (r - l + 1) - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        
        return m
