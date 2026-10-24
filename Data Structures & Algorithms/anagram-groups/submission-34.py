class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # {numerical values : [a1, a2, .. an]}

        # curString = {c: 1, a: 1, t: 1}
        # charMap = {c: 1, a: 1, t: 1} : ['cat', 'act' ]

        charMap = defaultdict(list)

        for s in strs:
            curString = defaultdict(int)
            for c in s:
                curString[c] += 1
            charMap[tuple(sorted(curString.items()))].append(s)

        ret = []

        for string in charMap.values():
            ret.append(string)

        return ret
