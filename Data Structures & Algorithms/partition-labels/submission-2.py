class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        start, part = 0, 0
        res = []
        for end in range(len(s)):
            part = max(part, last[s[end]])
            
            if end == part:
                res.append(end - start + 1)
                start = end + 1
            

        return res