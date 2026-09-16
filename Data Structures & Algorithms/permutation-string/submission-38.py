class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = defaultdict(int)
        r, l = 0, 0
        # abcl
        # daokbacdl
        # 

        for c in s1:
            charMap[c] += 1

        
        while r < len(s2):
            
            if r - l == len(s1):
                return True
            if s2[r] in charMap and charMap[s2[r]] > 0:
                charMap[s2[r]] -= 1
                r += 1
            elif r - l > 0:
                charMap[s2[l]] += 1
                l += 1
            else:
                r += 1
                l += 1

        return r - l == len(s1)