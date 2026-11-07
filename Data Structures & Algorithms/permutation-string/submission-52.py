class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        if n < m: return False
        l, r = 0, 0
        freq = Counter(s1)
        # s2 = zzzabbbabc s1 = abc
        #             l r
        while r < n:
            
            if s2[r] in freq and freq[s2[r]] > 0:
                freq[s2[r]] -= 1
                r += 1
            elif l < r: # Window is partially built
                freq[s2[l]] += 1
                l += 1
            else: # No window built
                r += 1
                l = r
            if r - l == m and not any(freq.values()): # Slowish
                return True

        return False