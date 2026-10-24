class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        charMap = defaultdict(list)

        for s in strs:
            curString = [0] * 26
            for c in s:
                curString[ord(c) - ord('a')] += 1
            charMap[tuple(curString)].append(s)

        return list(charMap.values())
