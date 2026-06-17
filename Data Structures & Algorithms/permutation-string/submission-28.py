class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def pos(char):
            return ord(char) - ord('a')
        freq, l, r = [0] * 26, 0, 0
        for c in s1:
            freq[pos(c)] += 1

        while r < len(s2) and r - l < len(s1):
            if freq[pos(s2[r])]:
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
