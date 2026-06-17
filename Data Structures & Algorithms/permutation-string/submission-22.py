class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = abc, s2 = abebad
        #                 
        # [0, 0, 0...0]
        freq = [0] * 26
        l, r = 0, 0
        def pos(char):
            return ord(char) - ord('a')

        for c in s1:
            freq[pos(c)] += 1

        while r < len(s2):
            if r - l == len(s1):
                return True
            elif freq[pos(s2[r])]:
                freq[pos(s2[r])] -= 1
                r += 1
                print(s2[l:r], r)
            elif l == r:
                l += 1
                r += 1
            else:
                freq[pos(s2[l])] += 1
                l += 1
        return r - l == len(s1)
