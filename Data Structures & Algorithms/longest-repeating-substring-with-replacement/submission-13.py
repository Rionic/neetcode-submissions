class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        l, longest = 0, 0
        # AABAABAAAAA    1
        for r in range(len(s)):
            windowLen = r - l + 1
            charCount[s[r]] += 1
            print(charCount)
            print(windowLen - max(charCount.values()))
            print('maxlen', longest)
            if windowLen > longest:
                if windowLen - max(charCount.values()) <= k:
                    longest = windowLen
                else:
                    charCount[s[l]] -= 1
                    l += 1
        return longest

        