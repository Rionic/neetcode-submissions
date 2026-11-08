class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        charMap = Counter(s)

        l, r = 0, 0
        res = []
        partition = defaultdict(int)
        while r < len(s): # Check this works later

            if r == l: # Start new partition/window
                partition[s[r]] = charMap[s[r]] - 1
            elif partition: # Might also be able to just check if all values == 0 and remove if: del block
                if s[r] not in partition:
                    partition[s[r]] = charMap[s[r]]
                partition[s[r]] -= 1
            if partition[s[r]] == 0:
                del partition[s[r]]
            if not partition: # Partition complete
                res.append(r - l + 1)
                l = r + 1
            
            r += 1

        return res