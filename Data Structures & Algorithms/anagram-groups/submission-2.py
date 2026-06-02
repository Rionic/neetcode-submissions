class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            charmap = [0] * 26
            for c in s:
                charmap[ord(c) - ord('a')]+=1
            res[tuple(charmap)].append(s)
        return list(res.values())
