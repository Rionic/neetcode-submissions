class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:

            charMap = [0] * 26
            for c in s:
                charMap[ord(c) - ord('a')] += 1

            res[tuple(charMap)].append(s)

        return list(res.values())
            
                