class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # {numerical values : [a1, a2, .. an]}

        # curString = {c: 1, a: 1, t: 1}
        # charMap = {c: 1, a: 1, t: 1} : ['cat', 'act' ]

        charMap = defaultdict(list)

        for s in strs:
            curString = [0] * 26
            for c in s:
                curString[ord(c) - ord('a')] += 1
            charMap[tuple(curString)].append(s)

        ret = []

        for string in charMap.values():
            ret.append(string)

        return ret
