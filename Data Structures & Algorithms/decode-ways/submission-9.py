class Solution:
    def numDecodings(self, s: str) -> int:
        # 12345 -> 1,2,3,4,5 | 1,2,3,45
        # At each position i in the string, we each take the singular number, or combine it with its neighbour
        # When combining, need to check 1 <= num <= 26, otherwise invalid
        # Cache: how many ways can we decode the subchunk e.g. 1234 + 231. 231 has 2 ways
        one = 1
        two = 1
        for i in range(len(s) -1, -1, -1):
            total = 0
            if s[i] != '0':
                total += one

            if s[i] != '0' and i + 1 < len(s) and 1 <= int(s[i] + s[i + 1]) <= 26:
                total += two
            
            two = one
            one = total

        return one
