class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len, l, r = 0, 0, 0
        charMap = defaultdict(int)

        for r in range(len(s)):

            charMap[s[r]] += 1
            while r - l + 1 - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            max_len = max(r - l + 1, max_len)
        
        return max_len



        
