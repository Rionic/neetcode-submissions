class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1

            strMap[tuple(chars)].append(s)

        res = []

        for value in strMap.values():
            res.append(value)

        return res
