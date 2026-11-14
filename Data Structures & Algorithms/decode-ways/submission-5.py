class Solution:
    def numDecodings(self, s: str) -> int:
        # 12345 -> 1,2,3,4,5 | 1,2,3,45
        # At each position i in the string, we each take the singular number, or combine it with its neighbour
        # When combining, need to check 1 <= num <= 26, otherwise invalid
        # Cache: how many ways can we decode the subchunk e.g. 1234 + 231. 231 has 2 ways
        cache = {len(s): 0}

        def dfs(i):
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]
            total = 0
            # Select singular element
            if s[i] != '0':
                total += dfs(i + 1)

            # Select two elements if valid
            if s[i] != '0' and i + 1 < len(s) and 1 <= int(s[i] + s[i + 1]) <= 26:
                total += dfs(i + 2)

            cache[i] = total

            return cache[i]
        
        return dfs(0)
