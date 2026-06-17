class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "aaaab", s2 = "abcdeabcdef"
        # a: 1
        # b: 1
        # c: 1
        #
        import copy
        charMap = defaultdict(int)

        for s in s1:
            charMap[s] += 1

        charMap2 = copy.deepcopy(charMap)
        
        for l in range(len(s2)):
            while l < len(s2) and charMap2[s2[l]] > 0:
                charMap2[s2[l]] -= 1
                l += 1
            if all(v == 0 for v in charMap2.values()):
                return True
            charMap2 = copy.deepcopy(charMap)

        return False