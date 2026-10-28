class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charMap = [0] * 26
        l, r = 0, 0

        for c in s1:
            charMap[ord(c) - ord('a')] += 1

        # lze
        # lzcabee
        #   r

        while r < len(s2): # last element edge case?
            cur = ord(s2[r]) - ord('a')
            # long's char is in short & unused
            if charMap[cur] != 0:
                charMap[cur] -= 1
                r += 1
            else:
                if l < r:
                    charMap[ord(s2[l]) - ord('a')] += 1
                else:
                    r += 1
                l += 1
            if r - l == len(s1):
                return True

        return False
